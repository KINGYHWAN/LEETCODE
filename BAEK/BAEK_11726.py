"""
1. 아이디어
 - 점화식 : An = An-1 + An-2
 - for 문으로 3부터 N까지 구해서 덧셈
 - 10007로 나눠 저장

2. 시간복잡도
 - O(N)

3. 자료구조
 - 배열 int[]


"""

import sys
input = sys.stdin.readline

N = int(input())

rs = [0, 1, 2]

for i in range(3, N+1):
    rs.append((rs[i-1] + rs[i-2])%10007)

print(rs[N])