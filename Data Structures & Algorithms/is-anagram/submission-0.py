class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        freq = {}
        for i in s:
            freq[i] = freq.get(i, 0) + 1
        
        for i in t:
            if freq.get(i, 0) > 0:
                freq[i] -= 1
            else:
                return False
        
        return True