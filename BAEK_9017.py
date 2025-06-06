from collections import Counter

def find_the_best_team(rank):
    cnt = Counter(rank)
    
    # 자격 있는 팀들 (6명 이상)
    team_set = set(team for team in cnt if cnt[team] >= 6)
    
    team_scores = {team: [] for team in team_set}
    
    # 등수는 1부터 시작
    score = 1
    for player in rank:
        if player in team_set:
            team_scores[player].append(score)
        score += 1

    result = {}
    for team in team_set:
        # 상위 4명 점수 합산
        total_score = sum(team_scores[team][:4])
        fifth_score = team_scores[team][4]  # 5번째 선수 점수 (tie-breaker용)
        result[team] = (total_score, fifth_score)
    
    # 점수 합산 → tie-break → 팀 번호 순
    best_team = min(result.items(), key=lambda x: (x[1][0], x[1][1], x[0]))[0]
    return best_team

# 입력 처리
case_num = int(input())
for _ in range(case_num):
    n = int(input())
    rank = list(map(int, input().split()))
    print(find_the_best_team(rank))
