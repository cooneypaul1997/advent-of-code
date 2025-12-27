import math
from collections import Counter

file_path = r"C:\Vibing\advent-of-code\2025\day08\real-input.txt"

with open(file_path) as f:
    file_contents = f.read().splitlines()

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]

points = [tuple(map(int, line.split(","))) for line in file_contents]
n = len(points)

edges = []
for i in range(n):
    x1, y1, z1 = points[i]
    for j in range(i + 1, n):
        x2, y2, z2 = points[j]
        d = math.sqrt(
            (x1 - x2) ** 2 +
            (y1 - y2) ** 2 +
            (z1 - z2) ** 2
        )
        edges.append((d, i, j))

edges.sort(key=lambda x: x[0])

connections = min(1000, len(edges))

uf = UnionFind(n)
for k in range(connections):
    _, i, j = edges[k]
    uf.union(i, j)

roots = [uf.find(i) for i in range(n)]
sizes = sorted(Counter(roots).values(), reverse=True)

result = sizes[0] * sizes[1] * sizes[2]
print("Circuit sizes:", sizes)
print("Result:", result)
