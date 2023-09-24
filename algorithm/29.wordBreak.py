class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [0] * (len(s)+1)
        dp[0] = 1
        for i in range(1, len(s)+1):
            for j in range(i):
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = 1
                    break
        if dp[-1]:
            return True
        else:
            return False

solution = Solution()
res = solution.wordBreak(s = "leetcode", wordDict = ["leet", "code"])
print(res)
                    