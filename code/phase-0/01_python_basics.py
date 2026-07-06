# парні числа
evens = [n for n in range(10) if n % 2 == 0]
print(evens)


def generator(n: int) -> int:
    for i in range(n):
        yield i * i


for v in generator(5):
    print(v)


# timer

import time


def timer(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()

        print(f"Time is {end - start:.4f}s")

    return wrapper


@timer
def slow_function():
    time.sleep(0.1)


slow_function()

# file reader

with open("assets/file.txt", "r") as f:
    content = f.read()
    print(content)

# type hints


def add(a: int, b: int) -> int:
    return a + b


print(add(4, 5))
