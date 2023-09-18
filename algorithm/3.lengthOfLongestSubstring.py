class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        i = 0
        j = 1
        result = 1
        while j<len(s):
            j_idx = s[i:j].find(s[j])
            if j_idx==-1:
                result = max(result, j-i+1)
            else:
                i = i+j_idx+1
            j += 1
        return result


solution = Solution()
s = "pwwkew"
res = solution.lengthOfLongestSubstring(s)
print(res)
