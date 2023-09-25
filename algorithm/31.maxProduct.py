class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        dp = [[0, 0] for _ in range(len(nums))]
        dp[0] = [nums[0], nums[0]]
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i])
            dp[i][1] = min(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i])
            result = max(result, dp[i][0])
        return result

solution = Solution()
solution.maxProduct(nums = [2,3,-2,4])
