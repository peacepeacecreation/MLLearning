import numpy as np

def loss(w=0.0, lr=0.1, n_iter=50):
    print(f"w = {w}, lr = {lr}")
    for i in range(n_iter):
        grad = 2*(w - 3)
        w -= lr * grad
        if i % 5 == 0:
            print(f"w = {w}, loss = {(w - 3)**2}")


print(loss(lr=0.1))
print(loss(lr=0.01))
print(loss(lr=1.0))
print(loss(lr=1.5))

X = np.random.randn(200)
Y = (3 * X - 2)
y_true = Y + 0.5 * np.random.randn(200)

print(X.shape)


def find_best_w(y_true, X, lr=0.1, n_iter=200):
   print(f"lr = {lr}")

   w = 0.0
   b = 0.0

   for i in range(n_iter):
       y_pred = w * X + b

       error = y_true - y_pred

       grad_w = -2 * np.mean(error * X)
       grad_b = -2 * np.mean(error)
       w -= lr * grad_w
       b -= lr * grad_b

       loss = np.mean(error**2)

       if i % 20 == 0:
           print(f"w={w}, b={b}, loss={loss}")


# find_best_w(y_true=y_true, X=X, lr=0.1, n_iter=200)


# Section 4
#

X = np.random.randn(200, 3)
true_w = np.array([2.0, -1.0, 0.5])
true_b = 3.0

y_true = (X @ true_w + true_b) + (0.3 * np.random.randn(200))

def find_best_x_b(y_true, X, lr=0.1, n_iter=200):
    w =  np.zeros(3)
    b =  0.0

    for i in range(n_iter):
        y_pred = X @ w + b

        error = y_true - y_pred

        grad_w = -2 * (X.T @ error) / len(error)
        grad_b = -2 * np.mean(error)

        w -= lr * grad_w
        b -= lr * grad_b

        loss = np.mean(error**2)

        if i % 20 == 0:
           print(f"w={w}, b={b}, loss={loss}")



#find_best_x_b(y_true=y_true, X=X, lr=0.1, n_iter=200)


# Section 6
#

X_norm = (X - X.mean(axis=0)) / X.std(axis=0)


find_best_x_b(y_true=y_true, X=X_norm, lr=0.1, n_iter=200)
