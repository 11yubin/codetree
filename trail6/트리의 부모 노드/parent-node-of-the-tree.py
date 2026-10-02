from collections import deque

n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Please write your code here.
graph = [[] for _ in range(n + 1)]
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n + 1)
visited = [False] * (n + 1)
visited[1] = True
q = deque([1])

while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            parent[nxt] = cur   # 처음 발견한 쪽이 부모
            q.append(nxt)

for i in range(2, n + 1):
    print(parent[i])