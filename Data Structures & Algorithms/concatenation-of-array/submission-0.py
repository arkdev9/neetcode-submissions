class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output = nums
        output.extend(nums)
        return output