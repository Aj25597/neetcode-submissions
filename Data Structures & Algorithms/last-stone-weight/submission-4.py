import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapified = heapq.heapify_max(stones)
        while len(stones) > 1:
            first = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)
            if first > second:
                heapq.heappush_max(stones,first-second)
            elif first == second:
                continue
            else:
                heapq.heappush_max(stones,second - first)
        
        return 0 if len(stones) == 0 else stones[0]