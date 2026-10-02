class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seens = {}
        seent = {}

        for i in s:
            seens[i] = seens.get(i, 0) + 1
        
        for i in t:
            seent[i] = seent.get(i, 0) + 1
        
        return seens == seent