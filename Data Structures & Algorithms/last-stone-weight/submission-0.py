import heapq
import math

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            stone_a = -1 * heapq.heappop(stones)
            stone_b = -1 * heapq.heappop(stones)
            diff = stone_a - stone_b
            if diff:
                heapq.heappush(stones, -1 * diff)

        return -1 * stones[0] if len(stones) else 0