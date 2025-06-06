from collections import defaultdict

def find_best_team(rank):
    team_counts = defaultdict(int)
    for team in rank:
        team_counts[team] += 1

    valid_teams = {team for team, count in team_counts.items() if count == 6}

    team_scores = defaultdict(list)
    score = 1
    for team in rank:
        if team in valid_teams:
            team_scores[team].append(score)
            score += 1

    result = []
    for team in valid_teams:
        scores = team_scores[team]
        total = sum(scores[:4])
        fifth = scores[4]
        result.append((total, fifth, team))

    result.sort()
    return result[0][2]

# 입력 처리
T = int(input())
for _ in range(T):
    N = int(input())
    rank = list(map(int, input().split()))
    print(find_best_team(rank))
