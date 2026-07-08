class TimeMap:

    def __init__(self):
        self.timemap = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.timemap.get(key):
            return ""

        left = 0
        right = len(self.timemap[key]) - 1

        best = ""

        while left <= right:
            mid = (left + right) // 2

            if self.timemap[key][mid][0] == timestamp:
                return self.timemap[key][mid][1]

            elif self.timemap[key][mid][0] < timestamp:
                best = self.timemap[key][mid][1]
                left = mid + 1

            elif self.timemap[key][mid][0] > timestamp:
                right = mid - 1
        
        return best

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)