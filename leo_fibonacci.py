#!/usr/bin/env python

import sys
import time

def iterative_fibonacci(n):
    if n < 2:
        return n
    previous_fibonacci = 1
    current_fibonacci = 1
    for num in range(2, n):
        previous_fibonacci, current_fibonacci = current_fibonacci, \
            current_fibonacci + previous_fibonacci
    return current_fibonacci

def recursive_fibonacci(n):
    if n < 2:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)


if len(sys.argv) < 1:
    print('Usage:')
    print('     python ' + sys.argv[0] + ' N')
    print('Please specify the number of iterations.')
    sys.exit()

def main():
    N = int(sys.argv[1])
    t0 = time.perf_counter()
    iterative_fibonacci(N)
    t1 = time.perf_counter()
    recursive_fibonacci(N)
    t2 = time.perf_counter()
    print(t1-t0,t2-t1,sep='\n')

if __name__ == "__main__":
    main()
