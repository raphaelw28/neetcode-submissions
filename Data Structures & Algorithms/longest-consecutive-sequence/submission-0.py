class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        my_set = set(nums)
        

        for n in my_set:
            if n - 1 not in my_set:
                counter = 1
                i = 1
                while (n + i) in my_set:
                    counter += 1
                    i += 1
                if counter > longest:
                        longest = counter
                
        return longest
        