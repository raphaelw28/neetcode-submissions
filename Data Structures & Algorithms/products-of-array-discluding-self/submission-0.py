class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer = [1]
        product = 1
        for i in range(1, len(nums)):
            product *= nums[i - 1]
            answer.append(product)
        
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= product
            product *= nums[i]

       
        return answer
        