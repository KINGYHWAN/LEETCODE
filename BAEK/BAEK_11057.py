"""

오르막수..


자릿수 == 1:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9

자릿수 == 2:
00, 01, 02
    11, 12
        22

"""

N = int(input())

dp = [1] * 10

for _ in range(N-1):
    for j in range(1, 10):
        dp[j] = dp[j] + dp[j-1]

print(sum(dp)%10007)
