class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        writer = 0

        for i in range(len(nums)):
            if nums[i] == val:
                continue
            
            nums[writer] = nums[i]
            writer = writer + 1
        
        return writer