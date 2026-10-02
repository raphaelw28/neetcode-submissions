class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num

            if complement not in seen:
                seen[num] = i
            else:
                return [seen[complement], i]