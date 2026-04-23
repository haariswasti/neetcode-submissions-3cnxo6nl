class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ## we need each value to be the product of itis surrodning value
        #create the values and multiply everything before and after
        prefix = 1
        prelist = [1] * len(nums)

        for i in range(len(nums)):
            prelist[i] = prefix
            prefix *= nums[i]

        postfix = 1
        

        for i in range(len(nums)-1 , -1, -1):
            prelist[i] *= postfix
            postfix *= nums[i]
        return prelist


        