import numpy as np

def cosine_sim(a, b):
    return a @ b / (np.linalg.norm(a) * np.linalg.norm(b))
