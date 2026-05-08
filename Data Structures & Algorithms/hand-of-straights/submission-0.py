class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        cnt_map = defaultdict(int)
        for v in hand:
            cnt_map[v] += 1
        
        hand.sort()
        
        for num in hand:
            if cnt_map[num]:
                for v in range(num, num+groupSize):
                    if v not in cnt_map or cnt_map[v] == 0:
                        return False
                    cnt_map[v] -= 1
        return True