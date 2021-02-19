class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = []
        for i in range(len(nums)):
            if nums[i] == 0:
                idx.append(i)
        
        idx.reverse()
        for i in idx:
            nums.pop(i)
            nums.append(0)
