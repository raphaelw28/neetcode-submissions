class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        best = 0
        l = 0
        

        for i, t in enumerate(s):
            while t in seen:
                seen.remove(s[l])
                l += 1
            seen.add(t)
            best = max(best, i - l + 1)
        
        return best
            
                

