from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_counts = defaultdict(int)
        prefix_sum_counts[0] = 1
        cumsum = 0
        ans = 0

        for num in nums:
            cumsum += num
            netsum = cumsum - k
            ans += prefix_sum_counts[netsum]
            
            prefix_sum_counts[cumsum] += 1

        return ans