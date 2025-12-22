"""
1. IDEA
 - sort
 - for 문 돌면서 search() 진행해서 있는지 확인

2. Time Complexity
 - sort : N log N
 - search M log N
 - (N+M)logN

3. data structure
 - List

"""

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))


nums.sort()

def search(start, end, target):

    if start == end:
        if nums[start] == target:
            print(1)
        else:
            print(0)
        return
    
    mid = (start + end) // 2
    if nums[mid] < target:
        search(mid+1, end, target)
    else:
        search(start, mid, target)


for target in targets:
    
    search(0, N-1, target)



