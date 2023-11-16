# https://www.acmicpc.net/problem/11720
import sys

input = sys.stdin.readline

n = input()
nums = list(input())
sum = 0

for n in nums:
    sum += int(n)

print(sum)