class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = []
        ans = []
        use = [False] * len(nums)
        def backtrack():
            if len(perm) == len(nums):
                
                ans.append(perm[:])
                return
            
            for x in range(len(nums)):
                if use[x]:
                    continue
                perm.append(nums[x])
                use[x] = True
                backtrack()
                perm.pop()
                use[x] = False
        backtrack()   
        return ans


