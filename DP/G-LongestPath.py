# https://atcoder.jp/contests/dp/tasks/dp_g

import queue
from sys import setrecursionlimit

setrecursionlimit(10**7)

numNodes, numEdges = map(int, input().split())
nodes = []
entries = set()

for i in range(numNodes):
    nodes.append([])
    entries.add(i)

for _ in range(numEdges):
    s, e = map(int, input().split())
    nodes[s - 1].append(e - 1)
    if e - 1 in entries:
        entries.remove(e - 1)


distances = [None] * numNodes

def dfs(curNode):
    if distances[curNode] is not None:
        return distances[curNode]
    d = 0
    for neig in nodes[curNode]:
        d = max(d, dfs(neig) + 1)
    distances[curNode] = d
    return d

result = 0
for e in entries:
    result = max(result, dfs(e))

print(result)
