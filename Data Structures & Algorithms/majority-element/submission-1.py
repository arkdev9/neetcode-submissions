from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        print(counts)

        majority_key = None
        for c in counts:
            if majority_key is None:
                majority_key = c
                continue

            majority_key = c if counts[c] > counts[majority_key] else majority_key

        
        return majority_key