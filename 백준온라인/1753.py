# https://www.acmicpc.net/problem/1753

import sys
from queue import PriorityQueue

input = sys.stdin.readline

def solve(graph, distance, start_node, visited):
    que = PriorityQueue()
    # 최단 거리값부터 나오게 하기 위해서, (distance, next_node) 형태로 넣는다.
    que.put((0, start_node))

    while not que.empty():
        current = que.get()
        if visited[current[1]]:
           continue

        visited[current[1]] = True
        
        # 단절된 노드가 있을수 있기 때문에 예외처리를 한다.
        nexts = graph[current[1]] if current[1] in graph else []

        for tmp in nexts:
            value = tmp[0]
            next = tmp[1]

            # 계산된값 > 현재 거리 + next 노드까지의 거리 이면, 값을 업데이트 한다.
            if distance[next] > distance[current[1]] + value:
                distance[next] = distance[current[1]] + value

            # 중요!!, 해당 노드까지 누적합으로 넣어준다.
            que.put((distance[next], next))        

# 문제 입력 조건 처리
V, E = map(int, input().split())
START_NODE = int(input())
graph = {}
for ii in range(E):
    u, v, w = map(int, input().split())

    if u in graph:
        graph[u].append((w, v))
    else:
        graph[u] = [(w, v)]

# 방문 여부 체크 리스트
# node값이 1부터 시작하기 때문에 동일하게 처리하기 위해 size+1 리스트를 만든다
visited = [False] * (V + 1) 

# 노드별 거리 리스트
# 동일하게 size+1 으로 만들고, 최초 최대값을 넣는다
distance = [sys.maxsize] * (V + 1)

# 시작노드의 값은 0으로 셋팅하고 시작한다.
distance[START_NODE] = 0

solve(graph, distance, START_NODE, visited)

for ii in range(1, V+1):
    if visited[ii]:
        print(distance[ii])
    else:
        print('INF')