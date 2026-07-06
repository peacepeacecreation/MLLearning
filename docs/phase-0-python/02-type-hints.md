# 02 — Type hints + mypy

## Що це
Система анотацій типів у Python + інструмент mypy що перевіряє їх без запуску коду.

## Для чого
- IDE підказує помилки ще під час написання
- mypy знаходить баги до runtime — як TypeScript компілятор але окремий крок
- Код читається як документація: одразу видно що функція приймає і що повертає

## Розбір

### Базові анотації
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b
```

### Колекції
```python
def sum_list(numbers: list[int]) -> int:
    return sum(numbers)

def count_words(words: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for word in words:
        result[word] = result.get(word, 0) + 1
    return result
```
`list[int]` — список цілих. `dict[str, int]` — ключ рядок, значення ціле.  
`dict.get(key, 0)` — повертає значення або `0` якщо ключа немає (коротше ніж `if key in dict`).

### str | None
```python
def find_user(user_id: int) -> str | None:
    users = {1: "Martyn", 2: "Alice"}
    return users.get(user_id)
```
`str | None` — функція повертає або рядок, або `None`. Старий синтаксис: `Optional[str]` з `typing`.

### tuple
```python
def get_coords() -> tuple[float, float]:
    return (50.45, 30.52)
```
`tuple[float, float]` — рівно два float, порядок фіксований.

### Запуск mypy
```bash
mypy code/phase-0/02_type_hints.py          # звичайна перевірка
mypy --strict code/phase-0/02_type_hints.py  # суворий режим
```

### Приклад помилки mypy
```python
add("hello", 3)  # помилка!
# error: Argument 1 to "add" has incompatible type "str"; expected "int"  [arg-type]
```
mypy знайшов помилку без запуску — до runtime.

## Gotchas
- Python виконає код навіть з неправильними типами — mypy це окремий крок, не частина інтерпретатора
- `str | None` — синтаксис Python 3.10+. На 3.9 і нижче: `from typing import Optional` → `Optional[str]`
- `list[int]` в анотаціях — Python 3.9+. Раніше: `from typing import List` → `List[int]`
- `dict.get(key, 0)` повертає `int | None` без default — якщо не передати default, тип буде ширший
- f-string конвертує будь-який тип через `str()` автоматично. `"hello" + 1` — TypeError, f-string — ні

## Джерела
- [Python docs: typing](https://docs.python.org/3/library/typing.html)
- [mypy docs](https://mypy.readthedocs.io/en/stable/)
- [PEP 604 — str | None syntax](https://peps.python.org/pep-0604/)
