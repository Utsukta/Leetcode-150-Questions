#26. Remove Duplicates from Sorted Array
#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
#The relative order of the elements should be kept the same. 
#Then return the number of unique elements in nums.



class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #ISSUES
        #Uses a for loop to iterate through the list by index. 
        #.This can be inefficient because modifying a list while iterating over it can lead to skipping elements or unnecessary iterations
        #The nested while loop inside the for loop is less intuitive and can be harder to follow.
        #Higher complexity

        # for i in range(len(nums)): 
        #     while i + 1 < len(nums) and nums[i] == nums[i + 1]:
        #         nums.pop(i + 1)
        # print(nums)


        #More Efficient
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i + 1)
            else:
                i += 1
        return len(nums)

s= Solution()
Output=s.removeDuplicates([1,1,2])
print(Output)
