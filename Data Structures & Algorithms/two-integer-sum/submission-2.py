class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #dict with all the values tracking index n value
        #check through all once rather then each value every time
        #aim for not O(n^2)

        #add index and compliment
        
        track = {}

        for i in range(len(nums)):
            
            compliment = target - nums[i]
            if compliment in track:
                return [track[compliment], i]
            track[nums[i]] = i

            
             
        