class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hashmap:
        tamiMap = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in tamiMap:
                return [tamiMap[complement], index]

            tamiMap[num] = index


        #bruteforce: O(n²)
        """for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return[i,j]"""
