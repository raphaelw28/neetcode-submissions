class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        array = []
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        for i in range(len(nums) + 1):
            array.append([])
        
        for num, count in freq.items():
            array[count].append(num)
        
        result = []
        i = len(result) - 1

        while k > len(result):
            for num in array[i]:
                result.append(num)
                if len(result) == k:
                    return result
            i -= 1

        
        