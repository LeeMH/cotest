# https://www.acmicpc.net/problem/17298

import sys

input = sys.stdin.readline

N = int(input())
NUMS = list(map(int, input().split()))
answer = [-1] * N

stack = []

for ii in range(0, N):
    # 스택에 새로운 값보다 작은값이 존재하는지 체크하고 있다면 pop
    while stack and NUMS[stack[-1]] < NUMS[ii]:
        answer[stack.pop()] = NUMS[ii]

    # 현재 인덱스를 stack에 추가한다.
    stack.append(ii)

for ii in range(N):
    print(answer[ii], end = ' ')
