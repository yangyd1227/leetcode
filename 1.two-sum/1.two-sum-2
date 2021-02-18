class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remain = {}
        for i in range(len(nums)):
            if nums[i] in remain:
                # note that checking if nums[i] exists in key is O(1)
                return [remain[nums[i]], i]
            else:
                remain[ target - nums[i] ] = i
