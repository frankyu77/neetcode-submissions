import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.k = k

        for num in nums:
            heapq.heappush(self.minHeap, num)
        
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
