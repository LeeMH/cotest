# https://www.acmicpc.net/problem/11660
import sys

input = sys.stdin.readline

n, q = map(int, input().split())

# 문제로 주어진 테이블 생성
nums = [[0] * (n+1)]
for _ in range(0, n):
    row = [0]
    row.extend(list(map(int, input().split())))
    nums.append(row)

# 합계 테이블 초기화
sums = []
for _ in range(0, n+1):
    row = [0] * (n+1)
    sums.append(row)

# 합계 테이블 생성
for x in range(1, n+1):
    for y in range(1, n+1):
        sums[x][y] = nums[x][y] + sums[x-1][y] + sums[x][y-1] - sums[x-1][y-1]

# 문제의 횟수만큼 계산하여 출력한다.
for _ in range(0, q):
    x1, y1, x2, y2 = map(int, input().split())
    print(sums[x2][y2] - sums[x2][y1-1] - sums[x1-1][y2] + sums[x1-1][y1-1])