# https://www.acmicpc.net/problem/1197

import sys
from queue import PriorityQueue

input = sys.stdin.readline

# 노드Num의 대표 노드Num을 구해온다.
def find(node_num, parent):
    if node_num == parent[node_num]:
        return node_num
    else:
        parent[node_num] = find(parent[node_num], parent)
        return parent[node_num]
    
def solve(node_count, pq, parent):
    result = 0
    use_edge = 0
    # 노드수 - 1만큼 연결해야 모든 노드가 사이클없이 연결된다.
    while use_edge < node_count -1:
        v, s, e = pq.get()
        s_parent = find(s, parent)
        e_parent = find(e, parent)
        if s_parent != e_parent:            
            use_edge += 1
            result += v
            parent[e] = s

    return result


# 노드와 엣지 입력 처리
V, E = map(int, input().split())

# 엣지정보를 처리, 최소 거리를 우선 처리하기 위해 PriorityQueue를 사용
pq = PriorityQueue()
for _ in range(E):
    s, e, v = map(int, input().split())
    pq.put((v, s, e))

# 각 Node의 대표 노드 저장정보 
parent = [ii for ii in range(V+1)]
print(solve(V, pq, parent))
