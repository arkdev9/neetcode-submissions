class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(permutation):
            if len(nums) == 0:
                result.append(permutation.copy())
                return
            
            for i in range(len(nums)):
                popped = nums.pop(i)
                permutation.append(popped)
                dfs(permutation)
                nums.insert(i, popped)
                permutation.pop()

        dfs([])
        return result
                