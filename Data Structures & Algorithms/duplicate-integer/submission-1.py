class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
        '''
        #Solution 1
        unique = []
        while nums != []:
            for num in nums:
                if num in unique:
                    return True
                else:
                    unique.append(num)

        #Solution 2
        nums.sort()
        for num in nums:
            index = num.index()
            if num is nums[index + 1]:
                return true
            else:
                continue

        #Solution 3
        hashset = []
        for n in nums:
            if n not in hashset:
                hashset.append(n)
            elif nums is []:
                return False
            else:
                return True
        '''