from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timeStorage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeStorage[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.timeStorage[key]
        rsf = ""
        left, right = 0, len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            if timestamp < values[mid][0]:
                right = mid - 1
            elif timestamp >= values[mid][0]:
                rsf = values[mid][1]
                left = mid + 1
        return rsf
