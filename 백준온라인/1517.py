# https://www.acmicpc.net/problem/1517

import sys

input = sys.stdin.readline

def merge_sort(s, e):
    # 최소 단위로 쪼개진 경우 리턴
    if e - s < 2:
        return
    
    # 중간 지점을 구한다
    mid = s + (e -s) // 2

    # 왼쪽, 오른쪽을 각각 정렬한다.
    merge_sort(s, mid)
    merge_sort(mid, e)

    # 정렬된 값을 저장할 임시 리스트 
    tmp = []

    # 좌측, 우측 비교 인덱스
    index1 = s
    index2 = mid
    global answer

    # 좌측과 우측을 비교하며 작은값을 tmp 리스트에 저장
    while index1 < mid and index2 < e:
        if NUMS[index1] > NUMS[index2]:
            tmp.append(NUMS[index2])
            index2 += 1
            answer += mid - index1
        else:
            tmp.append(NUMS[index1])
            index1 += 1

    # 남아 있는 좌측의 값을 tmp 리스트에 저장
    while index1 < mid:
        tmp.append(NUMS[index1])
        index1 += 1

    # 남아 있는 우측의 값을 tmp 리스트에 저장
    while index2 < e:
        tmp.append(NUMS[index2])
        index2 += 1

    # 원본 배열에 tmp 리스트의 값을 저장
    NUMS[s:e] = tmp


N = int(input())
NUMS = list(map(int, input().split()))
answer = 0

merge_sort(0, N)

print(answer)