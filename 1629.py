import sys
import numpy as np

A, B, C = map(int, sys.stdin.readline().rstrip().split())

print(np.power(A, B)%C)