"""

아이디어
 - dict에 저장해두고
 - callings에서 이름이 불리면 dict에서 찾아주고, players에서 변경해주고, 다시 dict 업데이트
 
T-C
 - O(N * M)

"""

def solution(players, callings):
    
    name_to_index = {}
    for idx, name in enumerate(players):
        name_to_index[name] = idx
    
    for call in callings:
        idx = name_to_index[call]
        prev_name = players[idx-1]
        players[idx-1], players[idx] = players[idx], players[idx-1]
        name_to_index[call] = idx-1
        name_to_index[prev_name] = idx
        
        
    return players