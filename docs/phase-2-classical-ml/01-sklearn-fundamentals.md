# sklearn fundamentals: train/test split, Pipeline, data leakage

## Що це

Обробка сирих даних так, щоб можна було чесно оцінити модель на нових, ще не бачених прикладах. Ключові інструменти: `train_test_split` (ділить дані на дві частини), `Pipeline` (об'єднує кроки препроцесингу і модель в один об'єкт), і найважливіше — уникнення **data leakage** (коли інформація з тестових даних випадково "просочується" в процес навчання ще до фінальної оцінки).

## Для чого

Якщо оцінювати модель на тих самих даних, на яких вона тренувалась — це як здавати екзамен по задачах, які вивчив напам'ять. Результат виглядає чудово, але нічого не каже про те, як модель поведеться на реальних нових даних. Правило "спочатку розділи дані, потім вчи модель тільки на train-частині" — фундамент чесної оцінки будь-якої ML-моделі.

## Розбір

### Train/test split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

- `test_size=0.2` — 20% даних відкладаємо, не чіпаємо до фінальної перевірки.
- `random_state=42` — фіксує випадковість, щоб результат був відтворюваним.
- Порядок повернених значень: `X_train, X_test, y_train, y_test` — легко переплутати, варто звіряти.

### fit / transform / predict / score

- **Transformer** (наприклад `StandardScaler`): `fit` — вчить статистики (mean/std) з даних, `transform` — застосовує їх до (будь-яких) даних.
- **Estimator/модель** (наприклад `LinearRegression`): `fit` — вчить параметри моделі, `predict` — повертає прогноз, `score` — рахує метрику якості (R² для регресії).

`fit` **нічого корисного не повертає** крім самого об'єкта — трансформовані дані з'являються тільки після `transform`. `fit_transform` — це `fit` + `transform` за один виклик.

### Pipeline

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LinearRegression()),
])

pipe.fit(X_train, y_train)
pipe.score(X_test, y_test)
```

Pipeline **сам** усередині викликає `transform` (не `fit_transform`!) на test-даних при `.predict()`/`.score()` — тобі не треба пам'ятати цю деталь вручну. Це структурний захист від найнебезпечнішої помилки уроку.

### Data leakage — найважливіший gotcha

**Неправильно:**
```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)              # mean/std по ВСІХ даних
X_train, X_test = train_test_split(X_scaled, y)  # split ПІСЛЯ масштабування
```

**Правильно:**
```python
X_train, X_test, y_train, y_test = train_test_split(X, y)  # спочатку split
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)          # fit тільки на train
X_test = scaler.transform(X_test)                # transform, НЕ fit_transform
```

Помилка була в **порядку дій**: якщо порахувати `mean`/`std` по всіх даних одразу, а тільки потім розділити на train/test — test-частина вже вплинула на ці статистики ще до того, як модель хоч раз щось передбачила на ній. Результат — завищена (оптимістична) оцінка якості моделі, яка не повториться в реальному проді.

### R² — метрика якості регресії

```
R² = 1 - (SS_res / SS_tot)
```

- `SS_res` — сума квадратів помилок моделі (`Σ(y_реальне - y_передбачене)²`) — та сама формула, що чисельник MSE.
- `SS_tot` — сума квадратів помилок наївного прогнозу (завжди середнє значення `y`).

`R²=0.61` означає: модель зменшила помилку на 61% порівняно з "завжди кажи середнє". Це **не** accuracy і не відсоток правильних відповідей.

### Supervised vs unsupervised

Supervised — є `y` (правильна відповідь), модель вчиться її передбачати. Unsupervised — тільки `X`, модель сама шукає структуру (наприклад, групує схожі об'єкти — clustering).

## Gotchas

- **`fit_transform` на test замість `transform`** — головна причина data leakage.
- **`fit()` повертає сам об'єкт**, не трансформовані дані — `x = scaler.fit(x)` перезаписує дані на scaler.
- **Плутанина: z-score/нормалізація — це НЕ сама модель.** Це підготовка даних (препроцесинг). Модель (наприклад `w*x+b` + нелінійність у нейроні) — окремий шар, де відбувається реальне навчання параметрів.
- **Порядок повернених значень `train_test_split`** — `X_train, X_test, y_train, y_test`, легко переплутати.
- **Перевикористання змінних між логічно різними шматками коду** (наприклад `X_train` вже змасштабований в одному місці, потім використаний вдруге в іншому Pipeline) — призводить до подвійного масштабування. Не завжди ламає результат явно, але концептуально неправильно.
- **`uv run`** обов'язковий для запуску — звичайний `python3` не бачить пакети з `.venv`.

## Джерела

- scikit-learn User Guide — Pipelines and composite estimators
- scikit-learn User Guide — Data leakage (секція в Cross-validation guide)
- "Hands-On Machine Learning" (Géron), розділ 2 — той самий California housing датасет
- Власний код: `code/phase-2/01_sklearn_fundamentals.py`
