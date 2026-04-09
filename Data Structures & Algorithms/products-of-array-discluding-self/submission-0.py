class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #multiply everything on the right of it
        #multiply everything on the left of it...
        ones = [1] * len(nums)
        prefix = 1
    #[1 2 3 4]
    #[1 1 2 6]
        for i in range(len(nums)):
            ones[i] = prefix
            prefix *= nums[i]

        postfix = 1
    #[6 8 12 24]
        for i in range(len(nums)-1, -1, -1):
            ones[i] *= postfix
            postfix *= nums[i] 

        return ones


        