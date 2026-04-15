import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)

        ans = 0
        stor = 0
        while k > ans:
            stor = -heapq.heappop(nums)
            ans += 1
        return stor


        

        
        