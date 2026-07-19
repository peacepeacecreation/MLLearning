import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error


# w = (XᵀX)⁻¹ Xᵀy
#

california_housing = fetch_california_housing(as_frame=True)

X, y = california_housing.data, california_housing.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LinearRegression())
])

pipe.fit(X_train, y_train)

model = pipe.named_steps["model"]

print(f"Score: {pipe.score(X_test, y_test)}")

print(list(zip(X.columns, model.coef_)))
print(f"Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_}")




# Sections 3
#

scaler = pipe.named_steps["scaler"]
x_first_scaled = scaler.transform(X_test.iloc[[0]])
x_test_first = x_first_scaled @ model.coef_ + model.intercept_
x_test_second = pipe.predict(X_test.iloc[[0]])

print(f"x_test_first: {x_test_first}")
print(f"x_test_second: {x_test_second}")


# Section 4
#

y_pred = pipe.predict(X_test)
y_r2_score = r2_score(y_test, y_pred)

y_mean_squared_error = mean_squared_error(y_test, y_pred)

print(f"y_r2_score: {y_r2_score}")
print(f"y_mean_squared_error: {y_mean_squared_error}")


# Section 5
#

model_noscale = LinearRegression()
model_noscale.fit(X_train, y_train)

scaler2 = StandardScaler()
X_train_scaled = scaler2.fit_transform(X_train)
X_test_scaled = scaler2.transform(X_test)

model_scaled = LinearRegression()
model_scaled.fit(X_train_scaled, y_train)

r_noscale = model_noscale.score(X_test, y_test)
r_scaled = model_scaled.score(X_test_scaled, y_test)

print(f"r_noscale: {r_noscale}")
print(f"r_scaled: {r_scaled}")

print(f"Coeficient noscale: {model_noscale.coef_}")
print(f"Coeficient scaled: {model_scaled.coef_}")

print(f"X_train_scaled[:, 0].min(): {X_train_scaled[:, 0].min()}")
print(f"X_train_scaled[:, 0].max(): {X_train_scaled[:, 0].max()}")

print(f"np.abs(X_train_scaled[:, 0]) > 1).mean(): {(np.abs(X_train_scaled[:, 0]) > 1).mean()}")


# Section 6
#


X_train_corr = X_train.corr()
print(X_train_corr.shape)

def find_top_corr(x, corr = .7):
    return np.where(np.abs(x) > corr)

top_corr = find_top_corr(X_train_corr)

print(f"top_corr: {X_train_corr}")
