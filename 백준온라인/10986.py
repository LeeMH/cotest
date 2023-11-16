# https://www.acmicpc.net/problem/10986

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0
sums = [0] * n
remains = [0] * m

# 부분합을 구한다.
sums[0] = nums[0]
for i in range(1, n):
    sums[i] = sums[i-1] + nums[i]

# 부분합을 m으로 나눈 나머지의 결과로 업데이트 한다.
for i in range(n):
    remainder = sums[i] % m
    if remainder == 0:
        answer += 1
    remains[remainder] += 1

# 동일 숫자가 2개이상 존재한다면, 컴비네이션 만큼 답을 더해준다.
for i in range(m):
    if remains[i] > 1:
        answer += remains[i] * (remains[i] -1) // 2

print(answer)