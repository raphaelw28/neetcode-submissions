class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        for s in strs:
            word += str(len(s)) + "#" + s
        return word

    def decode(self, s: str) -> List[str]:
        i = 0
        word = []
        while i < len(s):
            j = i
            while s[j]  != "#":
                j += 1
            
            length = int(s[i:j])

            j += 1
            string = s[j : j + length]
            word.append(string)

            i = j + length
            
        return word