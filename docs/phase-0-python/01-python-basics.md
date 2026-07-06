# 01 — Python basics: ключові конструкції

## Що це
П'ять конструкцій Python які зустрічаються в ML-коді щодня: comprehensions, generators, decorators, context managers, type hints.

## Для чого
- **Comprehension** — стислий фільтр/трансформація колекцій (замість циклів)
- **Generator** — ліниве обчислення великих послідовностей, не завантажує все в пам'ять (батчі для навчання моделі)
- **Decorator** — обгортка поведінки функції: логування, таймінг, кешування
- **Context manager** — безпечне відкриття ресурсів: файли, з'єднання з БД
- **Type hints** — підказки для IDE і mypy, як TypeScript але не enforce в runtime

## Розбір

### List comprehension
```python
# TS: [0,1,...,9].filter(n => n % 2 === 0)
evens = [n for n in range(10) if n % 2 == 0]
# [0, 2, 4, 6, 8]
```

### Generator
```python
from collections.abc import Iterator

def squares(n: int) -> Iterator[int]:
    for i in range(n):
        yield i * i

for v in squares(5):
    print(v)  # 0 1 4 9 16
```
`yield` — пауза і видача значення. Функція продовжується при наступному виклику ітератора.

### Decorator
```python
import time

def timer(func):
    def wrapper(*args):          # closure — замикає func
        start = time.time()
        func(*args)              # *args розпаковує аргументи
        end = time.time()
        print(f"Time is {end - start:.4f}s")
    return wrapper               # return, не yield

@timer
def slow_function():
    time.sleep(0.1)

slow_function()  # Time is 0.1046s
```
`@timer` — синтаксичний цукор для `slow_function = timer(slow_function)`.

### Context manager
```python
with open("assets/file.txt", "r") as f:
    content = f.read()
    print(content)
```
`with` гарантує закриття файлу навіть при помилці. Аналог `try/finally` у JS.

### Type hints
```python
def add(a: int, b: int) -> int:
    return a + b

print(add(4, 5))  # 9
```
Синтаксис: `параметр: тип` і `-> тип` для повернення. Не виконуються в runtime — тільки для IDE та mypy.

## Gotchas
- `number` — це TypeScript. У Python: `int`, `float`, `str`
- Синтаксис: `def func() -> int:` — двокрапка **після** типу, не перед `->`
- `yield` vs `return`: `yield` = пауза і продовження (generator), `return` = завершення функції
- `func(*args)` — зірочка розпаковує аргументи. `func(args)` передасть кортеж як один аргумент
- Generator функція повертає `Iterator[int]`, а не `int` — type hint `-> int` неточний
- Шлях у `open()` відносний до директорії **звідки запускаєш** скрипт, не від файлу скрипту

## Джерела
- [Python docs: Expressions — yield](https://docs.python.org/3/reference/expressions.html#yield-expressions)
- [Python docs: typing](https://docs.python.org/3/library/typing.html)
- [Real Python: Decorators](https://realpython.com/primer-on-python-decorators/)
- [Real Python: Context Managers](https://realpython.com/python-with-statement/)
