import random
class Solution:
    def __init__(self, w: List[int]):
        self.arr = w
        total = sum(w)
        self.prob = [0] * len(w)
        for i in range(len(w)):
            weight = round(w[i] / total * 100)
            self.prob[i] = weight
        
        self.pick = []
        prev = 0
        for i, p in enumerate(self.prob):
            self.pick[prev : prev + p] = [i] * p
            prev = prev+p

    def pickIndex(self) -> int:
        return random.choice(self.pick)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()