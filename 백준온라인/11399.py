# https://www.acmicpc.net/problem/11399

import sys

input = sys.stdin.readline

N = int(input())
NUMS = list(map(int, input().split()))
SUMS = [0] * N
answer = 0

NUMS.sort()

SUMS[0] = NUMS[0]
for ii in range(1, N):
    SUMS[ii] = SUMS[ii-1] + NUMS[ii]

for ii in range(N):
    answer += SUMS[ii]

print(answer)

