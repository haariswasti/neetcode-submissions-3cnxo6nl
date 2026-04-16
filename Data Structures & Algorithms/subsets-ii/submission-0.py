class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset = []
        ans = []
        nums.sort()
        def backtrack(i):
            ans.append(subset[:])
            
            for x in range(i, len(nums)):
                if x > i and nums[x] == nums[x -1]:
                    continue
                subset.append(nums[x])
                backtrack(x + 1)
                subset.pop()
            
          

        backtrack(0)
        return ans
        