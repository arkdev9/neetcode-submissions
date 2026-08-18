import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -1 * num)
        
        ans = heap[0]
        for i in range(k):
            ans = -1 * heapq.heappop(heap)
        
        return ans