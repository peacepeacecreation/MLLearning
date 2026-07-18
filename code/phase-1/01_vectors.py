import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

def manhattan(a: np.ndarray, b: np.ndarray) -> float:
    return np.sum(np.abs(a - b))

print(manhattan(a, b))

print(np.linalg.norm(a - b, ord=1))



king = np.array([0.9, 0.1, 0.8, 0.2])
apple = np.array([0.1, 0.9, 0.05, 0.1])

#Скалярний добуток (dot product) — операція над двома векторами однакової довжини, що дає одне число:
# a · b = a[0]*b[0] + a[1]*b[1] + a[2]*b[2] + ...
# Тобто перемножуєш елементи попарно і додаєш усе разом. У NumPy: a @ b (символ @, не + і не -).

print(king @ apple)
print(np.dot(king, apple))

def cosine_sim(a: np.ndarray, b: np.ndarray) -> float:
    return (a @ b) / ( np.linalg.norm(a) * np.linalg.norm(b) )

print(cosine_sim(king, apple))
print( np.linalg.norm(a) * np.linalg.norm(b))


query = np.array([1.0, .5, .2])
candidates = [
  np.array([.9, .4, .3]),
  np.array([-1.0, .1, .9]),
  np.array([.5, .5, .5]),
]

def most_similar(query: np.array, candidates: list[np.array]) -> int:
  best_score = None
  best_index = 0

  for index, candidate in enumerate(candidates):
    sim = cosine_sim(query, candidate)

    if best_score is None or sim > best_score:
      best_score = sim
      best_index = index

  return best_index

print(most_similar(query, candidates))

def most_similar_2(query: np.array, candidates: list[np.array]) -> int:
    return int(np.argmax([cosine_sim(query, c) for c in candidates]))

print(most_similar_2(query, candidates))



a = np.array([1, 1])
b = np.array([1, -1])
print(a @ b)


# "Вектор — це список чисел, який можна уявити як стрілку з напрямком.
# Dot product і cosine similarity міряють кут між двома такими стрілками — чим менший кут, тим більша схожість.
# #У ML це дозволяє порівнювати embedding-и (значення слів/речень/документів) за смислом, а не за конкретними числами."
