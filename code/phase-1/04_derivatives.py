# ┌───────────────┬───────────┐
# │     f(x)      │   f'(x)   │
# ├───────────────┼───────────┤
# │ c (константа) │ 0         │
# ├───────────────┼───────────┤
# │ x             │ 1         │
# ├───────────────┼───────────┤
# │ x²            │ 2x        │
# ├───────────────┼───────────┤
# │ x^n           │ n·x^(n-1) │
# ├───────────────┼───────────┤
# │ e^x           │ e^x       │
# ├───────────────┼───────────┤
# │ ln(x)         │ 1/x       │
# └───────────────┴───────────┘
#
# Правила: (f+g)' = f'+g' (похідна суми = сума похідних), (c·f)' = c·f' (константа виноситься).
#
#
# f(x) = 5x³ + 2x - 7
# f'(x) = ??
#
# f(x) = (x + 1)²
# f'(x) = 2(x + 1) = x² + 2x + 1 = 2x + 2 + 0
# f'(x) = x² * ln(x)
#
# Правило: (f*g)' = f'*g + f*g'.
#
#
#
#  Тут
# f=x² (тобто f'=2x),
# g=ln(x) (тобто g'=1/x, з таблиці).
#
#  Підстав і спрости.
#
# f'(x) = 2x * 1/x = 2x / x = 2
#
#
#
#
#
#
# Приклад на дошці: y = sin(x²). Розкладаю: u = x², y = sin(u).
# - du/dx = 2x
# - dy/du = cos(u) = cos(x²)
# - dy/dx = dy/du * du/dx = cos(x²) * 2x

# Задача 2 (chain rule drill): знайди похідну:
# - f(x) = e^(x²)
# - f(x) = (3x+1)^5

# Спробуй розкласти на u і зовнішню функцію, як у прикладі.


def numerical_gradient(f, params, h=1e-5):
  result = {}

  for key in params:
    params_plus = params.copy()
    params_plus[key] = params[key] + h
    params_minus = params.copy()
    params_minus[key] = params[key] - h
    result[key] = (f(**params_plus) - f(**params_minus)) / (2 * h)

  return result


def f(x, y):
  return x**2 * y + x * y**2 + 5

params = {
  "x": 1.0,
  "y": 2.0,
}


res = numerical_gradient(f, params)
print(res)
