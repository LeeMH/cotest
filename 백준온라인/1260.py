# https://www.acmicpc.net/problem/1260

import sys
from collections import deque

input = sys.stdin.readline

def dfs(start_node):
    mydeque = deque()
    mydeque.append(start_node)
    answer = []
    visited = set()

    while mydeque:
        v = mydeque.pop()

        if v not in visited:
            visited.add(v)
            answer.append(v)

        if v not in graph:
            continue
        else:
            for ii in reversed(range(len(graph[v]))):
                mydeque.append(graph[v][ii])

    print(' '.join(map(str, answer)), end = '\n')


def bfs(start_node):
    mydeque = deque()
    mydeque.append(start_node)
    answer = []
    visited = set()

    while mydeque:
        print(mydeque)
        v = mydeque.popleft()

        if v not in visited:
            answer.append(v)
            visited.add(v)        

        if v not in graph:
            continue

        print(graph[v])

        for k in graph[v]:
            if k not in visited:
                mydeque.append(k)

    print(' '.join(map(str, answer)), end = '\n')


graph = {}

N, M, V = map(int, input().split())
for _ in range(M):
    NUMS = list(map(int, input().split()))
    if NUMS[0] in graph:
        graph[NUMS[0]].append(NUMS[1])        
    else:
        graph[NUMS[0]] = [NUMS[1]]

dfs(V)
bfs(V)

