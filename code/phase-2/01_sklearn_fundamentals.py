from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression



# Section 1
#
data = fetch_california_housing(as_frame=True)
X, y = data.data, data.target

print(f"X: {X.shape}, y: {y.shape}")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

print(f"X_train: {X_train.shape}, X_test: {X_test.shape}, y_train: {y_train.shape}, y_test: {y_test.shape}" )




# Section 2
#
#

pipe = Pipeline([
  ("scaler", StandardScaler()),
  ("model", LinearRegression())
])

pipe.fit(X_train, y_train)

train_score = pipe.score(X_train, y_train)
test_score = pipe.score(X_test, y_test)

print(f"Train score: {train_score}, Test score: {test_score}")

# Section 3
#



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LinearRegression().fit(X_train, y_train)

print(model.score(X_test, y_test))


# Section 5
#

pipe2 = Pipeline([
  ("scaler", StandardScaler()),
  ("model", LinearRegression())
])

pipe2.fit(X_train, y_train)

print(pipe2.score(X_train, y_train))
print(pipe2.score(X_test, y_test))
