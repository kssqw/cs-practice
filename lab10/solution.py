import numpy as np


def make_table(rows: int, columns: int) -> list[list[int]]:
    return np.arange(rows * columns).reshape(rows, columns).tolist()


def rectangle(
    matrix: list[list[float]],
    row_start: int,
    row_stop: int,
    column_start: int,
    column_stop: int,
) -> list[list[float]]:
    arr = np.asarray(matrix)
    return arr[row_start:row_stop, column_start:column_stop].tolist()


def replace_rectangle(
    matrix: list[list[float]],
    row_start: int,
    row_stop: int,
    column_start: int,
    column_stop: int,
    value: float,
) -> list[list[float]]:
    arr = np.asarray(matrix).copy()
    arr[row_start:row_stop, column_start:column_stop] = value
    return arr.tolist()


def matrix_vector_product(
    matrix: list[list[float]],
    vector: list[float],
) -> list[float]:
    result = np.asarray(matrix) @ np.asarray(vector)
    return result.tolist()


def matrix_multiply(
    left: list[list[float]],
    right: list[list[float]],
) -> list[list[float]]:
    result = np.asarray(left) @ np.asarray(right)
    return result.tolist()


def transpose_matrix(matrix: list[list[float]]) -> list[list[float]]:
    return np.asarray(matrix).T.tolist()


def solve_system(
    matrix: list[list[float]],
    vector: list[float],
) -> list[float]:
    solution = np.linalg.solve(
        np.asarray(matrix, dtype=float),
        np.asarray(vector, dtype=float),
    )
    return np.round(solution, 6).tolist()

def tensor_channel_mean(tensor: list) -> list:
    arr = np.asarray(tensor, dtype=float)
    return arr.mean(axis=-1).tolist()


def point_distance(first: list[float], second: list[float]) -> float:
    diff = np.asarray(second, dtype=float) - np.asarray(first, dtype=float)
    return round(float(np.linalg.norm(diff)), 6)


