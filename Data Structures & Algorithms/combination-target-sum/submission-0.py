class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def backtrack(i, remain):
            if remain == 0:
                res.append(subset[:])
                return
            if i == len(nums) or remain < 0:
                return
            
            subset.append(nums[i])
            backtrack(i, remain - nums[i])
            subset.pop()
            backtrack(i + 1, remain)
        backtrack(0, target)
        return res


        








        