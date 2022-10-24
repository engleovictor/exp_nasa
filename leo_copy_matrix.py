#!/usr/bin/env pythons

import numpy as np
import sys
import time

def serial_copy(A):
    N = A.shape[0]
    for i in range(N):
        for j in range(N):
            A[i, j, 0] = A[i, j, 1]
            A[i, j, 2] = A[i, j, 0]
            A[i, j, 1] = A[i, j, 2]


def vector_copy(A):
    A[:, :, 0] = A[:, :, 1]
    A[:, :, 2] = A[:, :, 0]
    A[:, :, 1] = A[:, :, 2]


if len(sys.argv) < 1:
    print('Usage:')
    print('     python ' + sys.argv[0] + ' dimension')
    print('Please specify matrix dimensions')
    sys.exit()

def main():
    dimension = int(sys.argv[1])
    A = np.random.rand(dimension, dimension, 3)
    t0 = time.perf_counter()
    serial_copy(A)
    print(time.perf_counter() - t0)
    A = np.random.randn(dimension, dimension, 3)
    t0 = time.perf_counter()
    vector_copy(A)
    print(time.perf_counter() - t0)
    print()

if __name__ == "__main__":
    main()
