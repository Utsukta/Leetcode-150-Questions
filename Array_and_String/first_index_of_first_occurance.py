class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            needle_index=haystack.index(needle)
            return needle_index
        else:
            return -1
    
        
        
s=Solution()
output=s.strStr(haystack = "leetcode", needle = "leeto")
print(output)