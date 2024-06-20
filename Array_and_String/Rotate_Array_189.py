#189. Rotate Array
#Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

#Solution steps:
    # First we do mod, since sometimes k>len(nums)
    # Then, we take out the element which we take out from first to append it at last of array
    # Then, we empty the first r elements from the list 
    # then we extend the nums by element
    #Solution
        # k=k%len(nums)
        # r=len(nums)-k
        # element=nums[0:r]
        # nums[0:r]=[]
        # nums.extend(element)
        # return nums


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
    #nums[:-4]--- includ from starting and when it encounters-4 break and don't include -4 element
        #nums[-4:]-----  include -4 and start from -4 to last
        a=nums[-k%len(nums):]
        print(a)
        nums[:] = nums[-k%len(nums):] + nums[:-k%len(nums)]
      
	    
        return nums
        
s= Solution()
ouput=s.rotate([1,2,3,4,5,6,7],3)
print(ouput)