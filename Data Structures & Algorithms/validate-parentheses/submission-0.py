class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        arr = []

        for i in s:
            if i in my_dict:
                arr.append(i)  
            elif len(arr) == 0 or my_dict[arr.pop()] != i:
                    return False

        if len(arr) != 0:
            return False

        return True

            