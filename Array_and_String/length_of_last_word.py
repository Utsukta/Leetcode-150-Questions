class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # s = s.strip()
  
        return len(s.split()[-1]) if s else 0

        

s=Solution()
output=s.lengthOfLastWord("   fly me   to   the moon  ")
print(output)