from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        repQueue = deque()
        demQueue = deque()
        
        for i in range(n):
            if senate[i] == 'R':
                repQueue.append(i)
            else:
                demQueue.append(i)
                
        while repQueue and demQueue:
            repIndex = repQueue.popleft()
            demIndex = demQueue.popleft()
            if repIndex < demIndex:
                repQueue.append(repIndex + n)
            else:
                demQueue.append(demIndex + n)
                
        return "Radiant" if repQueue else "Dire"   