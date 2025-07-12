class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, item in enumerate(nums):
            if (target - item) in nums and nums.index(target - item) != index:
                position_1 = nums.index((target - item))
                position_2 = index
                return [position_1, position_2]
