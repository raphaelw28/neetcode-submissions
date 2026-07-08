class Solution:
    def maxArea(self, heights: List[int]) -> int:
        front = 0
        back = len(heights) - 1
        biggest = 0

        while front < back:
            current = ((back - front) * min(heights[front], heights[back]))
            if current > biggest:
                biggest = current 
            if heights[front] < heights[back]:
                front += 1
            else:
                back -= 1
        
        return biggest