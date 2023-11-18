# https://www.acmicpc.net/problem/1260

import sys
from collections import deque

input = sys.stdin.readline

def solve_dfs(graph, start_node):
    # 작은 값들부터 방문하기 위해서 역정렬한다.
    # 그래야 작은값이 stack의 최상위로 들어간다.
    for k in graph:
        nodes = graph[k] 
        nodes.sort(reverse = True)

    stack = [start_node]
    answer = []
    visited = set()

    while stack:
        v = stack.pop()

        if v not in visited:
            visited.add(v)
            answer.append(v)

        if v not in graph:
            continue
        else:
            for vv in graph[v]:
                if vv not in visited:
                    stack.append(vv)

    return ' '.join(map(str, answer))

def solve_bfs(graph, start_node):
    # bfs는 queue 방식으로 동작하기 때문에, 오름차순으로 정렬해서 넣는다.
    for k in graph:
        nodes = graph[k] 
        nodes.sort()

    queue = deque()
    queue.append(start_node)
    answer = []
    visited = set()

    while queue:
        v = queue.popleft()

        if v not in visited:
            answer.append(v)
            visited.add(v)

        if v not in graph:
            continue

        for k in graph[v]:
            if k not in visited:
                queue.append(k)

    return ' '.join(map(str, answer))


graph = {}

N, M, V = map(int, input().split())
for _ in range(M):
    NUMS = list(map(int, input().split()))

    if NUMS[0] in graph:
        graph[NUMS[0]].append(NUMS[1])        
    else:
        graph[NUMS[0]] = [NUMS[1]]

    if NUMS[1] in graph:
        graph[NUMS[1]].append(NUMS[0])
    else:
        graph[NUMS[1]] = [NUMS[0]]

print(solve_dfs(graph, V), end = '\n')
print(solve_bfs(graph, V), end = '\n')

