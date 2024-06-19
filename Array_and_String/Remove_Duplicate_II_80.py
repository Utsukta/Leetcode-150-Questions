class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #I wrote this code but not very efficient
        # i=0
        # while i<len(nums)-1:
        #     if nums[i]==nums[i+1]:
        #        i=i+1
        #        while i<len(nums)-1:
        #         if nums[i]==nums[i+1]:
        #           nums.pop(i+1)
        #         else:
        #            break
        #     else:
        #        i=i+1
        # return nums
                # The index for the next unique element
        
        #From sources
        if len(nums) <= 2:
            return len(nums)
        
        # Start from the third element
        j = 2
        
        for i in range(2, len(nums)):
            # If the current element is not equal to the element two positions before it
            if nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1
        
        return j

        
        
s=Solution()
output=s.removeDuplicates([1,1,1,1,2,2,2,2,2,3,4])
print(output)
