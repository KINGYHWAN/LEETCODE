n = int(input())
events = []

for _ in range(n):
    team, time = input().split()
    team = int(team)
    events.append((team, time))

def to_seconds(time_str):
    m, s = map(int, time_str.split(":"))
    return m * 60 + s

def to_time_str(seconds):
    m = seconds // 60
    s = seconds % 60
    return f"{m:02}:{s:02}"

score = [0, 0, 0]
lead_time = [0, 0, 0]
prev_time = 0

for team, now_time in events:

    if score[1] > score[2]:
        lead_time[1] += now_time - prev_time
    
    elif score[2] > score[1]:
        lead_time[2] += now_time - prev_time

    
    score[team] += 1
    prev_time = now_time

end_time = 48 * 60

if score[1] > score[2]:
    lead_time[1] += end_time - prev_time

elif score[2] > score[1]:
    lead_time[2] += end_time - prev_time


print(to_time_str(lead_time[1]))
print(to_time_str(lead_time[2]))