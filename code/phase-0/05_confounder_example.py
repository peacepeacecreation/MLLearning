"""
Приклад confounder problem на synthetic-даних.

Гіпотеза, яку симулюємо:
- Молоді (18-24) — переважно студенти або entry-level, часто без грошей на бар.
- Старші (25-50) мають стабільний дохід і ходять в бари вільно.
- Пиво п'ють переважно в барах, тому bar_visits → beer майже пряма залежність.

Що очікуємо побачити:
- corr(age, beer) — помірна додатна, бо старші п'ють більше пива.
- АЛЕ це через bar_visits як confounder (грошовий тригер).
- Партиальна кореляція age vs beer | control bar_visits → падає до ~0.

Це те саме що з fare/pclass/survived на Титаніку — не вік сам по собі,
а те що з ним корелює (грошові можливості → доступ до бару).
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

rng = np.random.default_rng(42)
N = 200

# --- 1. Генеруємо дані ---

# Вік від 18 до 50
age = rng.integers(18, 51, size=N)

# Молодь без стабільного доходу: 18-24 роки
young_no_income = age < 25

# Відсутність грошей на регулярні відвідування бару (bool → 0/1 для кореляції):
#  - 90% молодих (студенти, entry-level) фінансово обмежені
#  - 5% старших (безробіття, борги, форс-мажори)
no_money = np.where(
    young_no_income,
    rng.binomial(1, 0.9, size=N),
    rng.binomial(1, 0.05, size=N),
)

# Візити в бар за місяць:
#  - нема грошей → Пуассон з середнім 0.3 (майже не ходить)
#  - є гроші → Пуассон з середнім 4.0 (регулярний відвідувач)
bar_visits = np.where(
    no_money.astype(bool),
    rng.poisson(0.3, size=N),
    rng.poisson(4.0, size=N),
)

# Пиво (літри на місяць) = прямо пропорційне візитам + шум
beer_liters = bar_visits * 1.5 + rng.normal(0, 0.5, size=N)
beer_liters = np.clip(beer_liters, 0, None)  # не буває від'ємного

# --- 2. DataFrame ---

df = pd.DataFrame({
    "age": age,
    "no_money": no_money,
    "bar_visits": bar_visits,
    "beer_liters": beer_liters,
})

print("=== Перші 10 рядків ===")
print(df.head(10))
print()

# --- 3. Кореляційна матриця ---

corr = df.corr()
print("=== Матриця кореляцій ===")
print(corr.round(2))
print()

# --- 4. Heatmap ---

sns.heatmap(corr, annot=True, cmap="coolwarm", center=0, fmt=".2f")
plt.title("Кореляції: вік, відсутність грошей, візити в бар, пиво")
plt.tight_layout()
plt.show()

# --- 5. Partial correlation ---
# Формула: r(X,Y|Z) = (r_XY - r_XZ * r_YZ) / sqrt((1 - r_XZ²)(1 - r_YZ²))
# Це вимірює зв'язок X↔Y ПІСЛЯ вирахування впливу Z.

r_age_beer = df["age"].corr(df["beer_liters"])
r_age_bar = df["age"].corr(df["bar_visits"])
r_beer_bar = df["beer_liters"].corr(df["bar_visits"])

partial = (r_age_beer - r_age_bar * r_beer_bar) / np.sqrt(
    (1 - r_age_bar**2) * (1 - r_beer_bar**2)
)

print("=== Партиальна кореляція ===")
print(f"corr(age, beer)                         = {r_age_beer:.3f}")
print(f"corr(age, beer | control bar_visits)    = {partial:.3f}")
print()
print("Інтерпретація:")
print("- Перше число показує сирий зв'язок вік ↔ пиво (помірний додатний).")
print("- Друге число показує зв'язок ПІСЛЯ вирахування впливу bar_visits.")
print("- Якщо друге падає до ~0 — значить вік впливає на пиво ТІЛЬКИ через візити в бар.")
print("- Тобто bar_visits = confounder, а справжня причина —")
print("  відсутність грошей у молоді → менше візитів → менше пива.")

# --- 6. Візуалізація партиальної кореляції ---

# Розкидаємо людей на 3 групи по частоті візитів у бар
df["bar_group"] = pd.cut(
    df["bar_visits"],
    bins=[-1, 1, 3, 20],
    labels=["Low (0-1)", "Mid (2-3)", "High (4+)"],
)

# Кореляція age ↔ beer ВСЕРЕДИНІ кожної групи (має падати до ~0)
print("\n=== Кореляція age ↔ beer всередині груп однакового bar_visits ===")
for name, subset in df.groupby("bar_group", observed=True):
    if len(subset) > 5:
        r = subset["age"].corr(subset["beer_liters"])
        print(f"  {name} (n={len(subset)}): corr = {r:+.3f}")

# --- Графік 1: сирий scatter — видно висхідну хмару ---
sns.regplot(
    data=df,
    x="age",
    y="beer_liters",
    scatter_kws={"alpha": 0.5},
    line_kws={"color": "red"},
)
plt.title(f"Сирий scatter age ↔ beer\n(r = {r_age_beer:.2f}, є нахил)")
plt.tight_layout()
plt.show()

# --- Графік 2: розбиття по bar_visits — нахил всередині груп зникає ---
g = sns.lmplot(
    data=df,
    x="age",
    y="beer_liters",
    col="bar_group",
    height=4,
    aspect=0.9,
    scatter_kws={"alpha": 0.6},
    line_kws={"color": "red"},
)
g.fig.suptitle(
    "Всередині кожної групи bar_visits — залежність age→beer зникає\n"
    "(це і є суть партиальної кореляції: контролюємо confounder → сигнал падає)",
    y=1.08,
)
plt.tight_layout()
plt.show()
