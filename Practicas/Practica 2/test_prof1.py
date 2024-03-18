from algoritmos import caballo_profundidad_1
from collections import deque

n = 5
for x in range(n):
    for y in range(n):
        caballo_profundidad_1(n,deque([(x,y)]),deque([]))