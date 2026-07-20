import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

diabetes = load_diabetes(as_frame=True)
X, y = diabetes.data, diabetes.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipe = Pipeline([("scaler", StandardScaler()), ("model", LinearRegression())])
pipe.fit(X_train, y_train)
y_pred = pipe.predict(X_test)
r2 = r2_score(y_test, y_pred)

y_naive = np.full_like(y_test, y_train.mean())  # "завжди кажи середнє"
r2_naive = r2_score(y_test, y_naive)

fig, axes = plt.subplots(1, 2, figsize=(13, 6))

# --- Ліва панель: наша модель ---
ax = axes[0]
ax.scatter(y_test, y_pred, alpha=0.5, label="прогнози моделі")
lims = [min(y_test.min(), y_pred.min()), max(y_test.max(), y_pred.max())]
ax.plot(lims, lims, "r--", label="ідеальний прогноз (y=x)")
ax.axhline(y_train.mean(), color="gray", linestyle=":", label=f"наївний прогноз (mean={y_train.mean():.0f})")
ax.set_xlabel("Реальне значення (y_test)")
ax.set_ylabel("Прогноз моделі (y_pred)")
ax.set_title(f"Наша модель: R²={r2:.2f}")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.4)

# --- Права панель: наївний прогноз (завжди середнє) ---
ax = axes[1]
ax.scatter(y_test, y_naive, alpha=0.5, color="gray", label="наївний прогноз (завжди mean)")
ax.plot(lims, lims, "r--", label="ідеальний прогноз (y=x)")
ax.set_xlabel("Реальне значення (y_test)")
ax.set_ylabel("Прогноз (завжди середнє)")
ax.set_title(f"Наївний прогноз: R²={r2_naive:.2f}")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("code/phase-2/02c_r2_visualization.png", dpi=120)
print("saved to code/phase-2/02c_r2_visualization.png")
print(f"R² модель: {r2:.3f}, R² наївний прогноз: {r2_naive:.3f}")
