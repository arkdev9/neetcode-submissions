class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, current_comb):
            sum_current_comb = sum(current_comb)
            if i >= len(nums) or sum_current_comb > target:
                return
            if sum_current_comb == target:
                result.append(current_comb.copy())
                return
            
            current_comb.append(nums[i])
            dfs(i, current_comb)
            current_comb.pop()
            dfs(i + 1, current_comb)

        dfs(0, [])
        return result
