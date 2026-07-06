def greet(name: str) -> str:
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    return a + b


print(greet("Martyn"))


def sum_list(numbers: list[int]) -> int:
    return sum(numbers)


def find_user(user_id: int) -> str | None:
    users = {1: "Martyn", 2: "Alika"}
    return users.get(user_id)


print(sum_list([1, 2, 3]))
print(find_user(1))
print(find_user(99))


def count_words(words: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for word in words:
        result[word] = result.get(word, 0) + 1

    return result


print(count_words(["hey", "hey", "hello Martyn, how are you"]))
