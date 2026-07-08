class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False 

        freqs2 = {}
        freqs1 = {}
        first = 0

        for i in range(len(s1)):
            freqs2[s2[i]] = freqs2.get(s2[i], 0) + 1
            freqs1[s1[i]] = freqs1.get(s1[i], 0) + 1

        for i in range(len(s1), len(s2)):
            if freqs1 == freqs2:
                return True

            freqs2[s2[i]] = freqs2.get(s2[i], 0) + 1
            freqs2[s2[first]] -= 1

            if freqs2[s2[first]] == 0:
                del freqs2[s2[first]]

            first += 1



        return freqs1 == freqs2