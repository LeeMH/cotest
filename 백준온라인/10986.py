# https://www.acmicpc.net/problem/10986

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))

sums = [0]
for i in range(0, n):
    sums.append(sums[i] + nums[i])

count = 0
for i in range(1, n+1):
    for j in range(i, n+1):
        if (sums[j] - sums[i-1]) % m == 0:
            count += 1

print(count)