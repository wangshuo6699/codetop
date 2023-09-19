class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        count = 0
        result = float('-inf')
        while i < len(nums):
            count += nums[i]
            result = max(result, count)
            if count<0:
                count = 0
            i+=1
        return result


solution = Solution()
res = solution.maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,4])
print(res)
