class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        array = []

        for i in range(len(nums)):
            front = i + 1
            back = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            while front < back:
                 
                if nums[front] + nums[back] < -nums[i]:
                    front += 1
                elif nums[front] + nums[back] > -nums[i]:
                    back -= 1
                else: 
                    array.append([nums[i], nums[front], nums[back]])
                    front += 1
                    
                    while front < back and nums[front] == nums[front - 1]:
                        front += 1
        return array
        