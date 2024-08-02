import numpy as np
# Definición de las piezas y sus rotaciones utilizando matrices binarias
pieces = {
    "z": [
        np.array([[1, 1, 0], [0, 1, 1]], dtype=np.uint8),
        np.array([[0, 1], [1, 1], [1, 0]], dtype=np.uint8)
    ],
    "s": [
        np.array([[0, 1, 1], [1, 1, 0]], dtype=np.uint8),
        np.array([[1, 0], [1, 1], [0, 1]], dtype=np.uint8)
    ],
    "j": [
        np.array([[1, 0, 0], [1, 1, 1]], dtype=np.uint8),
        np.array([[1, 1], [1, 0], [1, 0]], dtype=np.uint8),
        np.array([[1, 1, 1], [0, 0, 1]], dtype=np.uint8),
        np.array([[0, 1], [0, 1], [1, 1]], dtype=np.uint8)
    ],
    "l": [
        np.array([[0, 0, 1], [1, 1, 1]], dtype=np.uint8),
        np.array([[1, 0], [1, 0], [1, 1]], dtype=np.uint8),
        np.array([[1, 1, 1], [1, 0, 0]], dtype=np.uint8),
        np.array([[1, 1], [0, 1], [0, 1]], dtype=np.uint8)
    ],
    "i": [
        np.array([[1, 1, 1, 1]], dtype=np.uint8),
        np.array([[1], [1], [1], [1]], dtype=np.uint8)
    ],
    "t": [
        np.array([[0, 1, 0], [1, 1, 1]], dtype=np.uint8),
        np.array([[1, 0], [1, 1], [1, 0]], dtype=np.uint8),
        np.array([[1, 1, 1], [0, 1, 0]], dtype=np.uint8),
        np.array([[0, 1], [1, 1], [0, 1]], dtype=np.uint8)
    ],
    "o": [
        np.array([[1, 1], [1, 1]], dtype=np.uint8)
    ]
}