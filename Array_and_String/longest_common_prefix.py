class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        words=strs
        if not words:
            return ""

    # Start with the first word as a base prefix
        prefix = words[0]

        # Iterate over the remaining words
        for word in words[1:]:
            # Compare the current prefix with the word until they match
            while not word.startswith(prefix):
                # Trim the last character from the prefix
                prefix = prefix[:-1]
                # If prefix becomes empty, there's no common prefix
                if not prefix:
                    return ""
        
        return prefix
        


s=Solution()
output=s.longestCommonPrefix(["flower","flow","flight"])
print(output)