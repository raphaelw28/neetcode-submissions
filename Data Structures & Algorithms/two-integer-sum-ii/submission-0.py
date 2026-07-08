class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front = 0
        back = len(numbers) - 1

        while back > front:
            if numbers[back] + numbers[front] < target:
                front += 1
            elif numbers[back] + numbers[front] > target:
                back -= 1
            
            if numbers[back] + numbers[front] == target:
                return [front + 1, back + 1]
        