from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

diabetes = load_diabetes(as_frame=True)
X = diabetes.data
y = diabetes.target

print(X.shape, y.shape)
print(X.columns.tolist())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipe = Pipeline([
  ('scaler', StandardScaler()),
  ('model', LinearRegression())
])

pipe.fit(X_train, y_train)

r2 = pipe.score(X_test, y_test)


print(f"R²: {r2}")


y_pred = pipe.predict(X_test)
y_r2_score = r2_score(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

print(f"MSE : {mse}")

model = pipe.named_steps['model']

print(list(zip(X.columns, model.coef_)))


print(f"Висновок: R²={r2:.2f} означає, що модель пояснює приблизно {r2*100:.0f}% розкиду (варіативності) прогресування діабету між пацієнтами за допомогою цих 10 ознак. "
      f"Решта ~{(1-r2)*100:.0f}% розкиду залишається непоясненою цими ознаками (інші фактори, шум) — "
      f"це НЕ означає що 55% прогнозів помилкові чи що ми 'близькі до середнього на 55%'.")
