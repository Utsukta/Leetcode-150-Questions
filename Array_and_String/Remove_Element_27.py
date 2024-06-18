#Question
#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
#The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

#Solution Explanation
#1. List Comprehension:(offers a shorter syntax when you want to create a new list based on the values of an existing list.)

#The expression [x for x in nums if x != val] creates a new list containing all elements of nums that are not equal to val.
#nums[:] = ... assigns the new list back to nums in-place. The [:] syntax ensures that the modification affects the original list object.

#2. Return Statement:

#return len(nums) returns the length of the modified nums list, which now contains no instances of val


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        nums[:] = [x for x in nums if x != val]
        return len(nums)
    
