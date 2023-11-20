# https://www.acmicpc.net/problem/11404

import sys

input = sys.stdin.readline

def solve(node_count, nodes):
    # 플로이드-워셜 알고리즘을 수행한다.
    # [ii][jj] 지점의 값과 k지점을 경유하는 지점의 값을 비교하여 적으면 업데이트
    for k in range(1, node_count+1):
        for ii in range(1, node_count+1):
            for jj in range(1, node_count+1):
                if nodes[ii][jj] > nodes[ii][k] + nodes[k][jj]:
                    nodes[ii][jj] = nodes[ii][k] + nodes[k][jj]

N = int(input())
M = int(input())

# 초기값을 sys.maxsize로 초기화
nodes = [[ sys.maxsize for jj in range(N+1)] for ii in range(N+1)]

# 버스 노선이 중복된 값이 존재하기 때문에, node간 이동 값중 가장 작은값으로 업데이트 한다.
for _ in range(M):
    source, to, value = map(int, input().split())
    if nodes[source][to] > value:
        nodes[source][to] = value

for ii in range(1, N+1):
    nodes[ii][ii] = 0

solve(N, nodes)

for ii in range(1, N+1):
    for jj in range(1, N+1):
        if nodes[ii][jj] == sys.maxsize:
            print(0, end = ' ')
        else:
            print(nodes[ii][jj], end = ' ')        
    
    print()