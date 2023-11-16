# https://www.acmicpc.net/problem/11003

import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
NUMS = list(map(int, input().split()))
mydeque = deque()

answer = []

for ii in range(N):
    # 들어가려고 하는 값보다 큰값이 있다면 계속 제거한다.
    while mydeque and mydeque[-1][1] >= NUMS[ii]:
        mydeque.pop()
    
    # (index, 값) 형태로 넣는다.
    mydeque.append((ii, NUMS[ii]))

    # 첫번째 원소가 윈도우 사이즈를 초과하는지 체크하고 초과시 제거
    if mydeque[0][0] <= ii - L:
        mydeque.popleft()

    print(mydeque[0][1], end = ' ')
