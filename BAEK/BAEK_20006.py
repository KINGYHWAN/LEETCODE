p, m = map(int, input().split())

rooms = []

for _ in range(p):
    level, name = input().split()
    level = int(level)

    entered = False
    for room in rooms:
        if len(room) < m and abs(room[0][0] - level) <= 10:
            room.append((level, name))
            entered = True
            break

    if not entered:
        rooms.append([(level, name)])

for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")

    for l, n in sorted(room, key = lambda x: x[1]):
        print(l, n)