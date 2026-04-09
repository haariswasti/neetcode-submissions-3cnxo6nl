class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #dict with all the values tracking index n value
        #check through all once rather then each value every time
        #aim for not O(n^2)
        track = {}

        for length in range(len(nums)):
            complement = target - nums[length]

            if complement in track:
                return [track[complement], length]

            track[nums[length]] = length





        