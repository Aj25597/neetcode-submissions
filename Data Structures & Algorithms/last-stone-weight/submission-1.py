class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            #Get first max
            first_idx = stones.index(max(stones))
            first_max = stones.pop(first_idx)
            #Get second max
            second_idx = stones.index(max(stones))
            second_max = stones.pop(second_idx)
            #Once we do that we want to figure out which one is bigger 
            if first_max >= second_max:
                #First bigger than second, sub and reinsert at idx it was at
                newMath = first_max - second_max
            else:
                newMath = second_max - first_max
            stones.append(newMath)
        return stones[0]