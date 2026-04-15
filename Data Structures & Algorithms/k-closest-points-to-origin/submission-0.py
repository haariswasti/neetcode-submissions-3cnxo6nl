import heapq
 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x = point[0]
            y = point[1]
            dsit = x * x + y * y
            heap.append((dsit, point))
        heapq.heapify(heap)

        res = []

        for _ in range(k):
            dsit, point = heapq.heappop(heap)
            res.append(point)
        return res

    

