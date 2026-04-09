class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #going to make a dict that tracks occurences of number
        #numbers that pop up the most return k....
        # how to check highest value in dict???

        sort = {}

        for num in nums:
            if num in sort:
                sort[num] += 1
            else:
                sort[num] = 1
        
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in sort.items():
            bucket[freq].append(num)
        ans = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans


        