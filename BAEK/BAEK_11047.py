"""

IDEA
 - reverse() 
 - 큰 수부터 갯수 세서 추가
 
"""

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]
coins.reverse()

cnt = 0

for each_coin in coins:
    cnt += K // each_coin
    K = K % each_coin

print(cnt)