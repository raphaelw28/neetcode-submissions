class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        first = 0
        longest = 0
        freq = {}

        for i, ch in enumerate(s):
            freq[ch] = freq.get(ch, 0) + 1
            max_freq = max(freq.values())
            
            while (i - first + 1) - max_freq > k:
                freq[s[first]] -= 1
                first += 1
            longest = max(longest, (i - first + 1))
        
        return longest
