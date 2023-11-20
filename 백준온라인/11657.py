# https://www.acmicpc.net/problem/1260

import sys

input = sys.stdin.readline

def solve(node_count, edges, visited, distance):
    has_cycle = False

    # 벨만포드 알고리즘은 노드수-1 횟수만큼 반복하면 최단거리가 발견된다.
    for _ in range(node_count -1):
        for source, to, time in edges:
            if not visited[source]:
                continue
            # 계산된 목적지 시간 > 현재노드까지 누적시간 + 해당노드로 이동시간 이라면 업데이트
            if distance[to] > distance[source] + time:
                distance[to] = distance[source] + time
                visited[to] = True
    
    # 음수 사이클이 존재하는지 확인하기 위해, 1회 더 실행
    # 이때 업데이트 되는 경로가 있다면 음수사이클이 존재하는것이다.    
    for source, to, time in edges:
        if not visited[source]:
            continue
        if distance[to] > distance[source] + time:
            has_cycle = True
            break
    
    return has_cycle


N, M = map(int, input().split())
edges = []
for _ in range(M):
    source, to, time = map(int, input().split())
    edges.append((source, to, time))

visited = [False] * (N + 1)
distance = [sys.maxsize] * (N + 1)
distance[1] = 0
visited[1] = True

has_cycle = solve(N, edges, visited, distance)
if has_cycle:
    print(-1)
else:
    for ii in range(2, N+1):
        print(distance[ii] if visited[ii] else -1)
