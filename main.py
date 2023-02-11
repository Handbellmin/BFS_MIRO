import sys
from collections import deque

input = sys.stdin.readline
graph = []
n, m = map(int, input().split())
for _ in range(n):
  graph.append(list(map(int, input().rstrip())))

#좌우상하
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(x, y):
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
        queue.append((nx, ny))
        graph[nx][ny] = graph[x][y] + 1
  return graph[n - 1][m - 1]


print(BFS(0, 0))
