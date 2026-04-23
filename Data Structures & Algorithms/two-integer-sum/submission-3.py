class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        #array of ints
        #target value
        #indicies i and j that sum up to the target....
        #every array has only one solution
        #brute force two nested loops O(n^2) 
        #hash map use a dictionary store the keys and value and
        #return the two indicies that store it

        store = {}

        for idx in range(len(nums)):
            
            comp = target - nums[idx]
            if comp in store:
                return [store[comp], idx]

            store[nums[idx]] = idx


             
        