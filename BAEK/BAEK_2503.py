from itertools import permutations

n = int(input())
questions = [tuple(map(int, input().split())) for _ in range(n)]

candidates = list(permutations(range(1, 10), 3))
count = 0

for candidate in candidates:
    is_possible = True
    for num, strike, ball in questions:
        num = list(map(int, str(num)))
        s = b = 0
        for i in range(3):
            if candidate[i] == num[i]:
                s += 1
            elif candidate[i] in num:
                b += 1
            
        if s != strike or b != ball:
            is_possible = False
            break
    if is_possible:
        count += 1

print(count)