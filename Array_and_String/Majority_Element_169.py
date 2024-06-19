#169. Majority Element

#Inefficient one
# import math as m
# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         length=m.floor(len(nums)/2)
#         print(length)
#         i=0
#         nums=sorted(nums)
#         while i<len(nums)-1:
#             if nums[i]!=nums[i+1]:
#                 count=i+1
#                 i+=1
#                 print(count)
#                 if count>length:
#                     element=nums[i-1] 
#                     return element  
#             else:
#                 element=nums[i]
#                 i+=1
#         return element



#Boyer-Moore Voting Algorithm to find the majority algorithm
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate
      

s=Solution()
output=s.majorityElement([6,6,6,7,7,])
print(output)



#Notes: In a sorted array, the majority element is guaranteed to be at the middle index if it appears more than ⌊n/2⌋ times.
#By sorting
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         n = len(nums)
#         return nums[n//2] middle element