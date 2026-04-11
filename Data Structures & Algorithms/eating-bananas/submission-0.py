class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #track the avg eating speed
        #at eating speed how many hours per pile
        #check if 
        left = 1 
        right = max(piles)
        ans = right

        while left <= right:
            k = (left + right)//2
            hours = 0

            for pile in piles:
                
                hours += (pile + k-1)//k

            if hours <= h:
                ans = k
                right = k -1
            else:
                left = k + 1
        return ans

        