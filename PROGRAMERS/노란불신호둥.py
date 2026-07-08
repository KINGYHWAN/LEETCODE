"""
1. 아이디어
 - 각 신호등의 Least Common Multiple (LCM) 구해서 주기 구함
 - 주기 구한 후 주기에 대해 각 list 별로 G < pos <= G+Y 확인 후 전부 True -> True 반환

2. 시간복잡도
 - O(N)

3. 자료구조
 - List[List[int]]


"""

import math

def solution(signals):
    periods = [sum(sig) for sig in signals]
    
    lcm = 1
    for p in periods:
        lcm = lcm * p // math.gcd(lcm, p)

    def is_yellow(t, sig):
        G, Y, R = sig
        period = G + Y + R
        pos = t % period
        if pos == 0:
            pos = period
        return G < pos <= G + Y

    for t in range(1, lcm + 1):
        all_yellow = True
        for sig in signals:
            if not is_yellow(t, sig):
                all_yellow = False
                break
        if all_yellow:
            return t

    return -1


    