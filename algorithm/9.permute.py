class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path = []
        result = []
        self.backtracking(nums, path, [0]*len(nums), result)
        return result

    def backtracking(self, nums, path, used, result):
        if len(path)==len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = 1
            path.append(nums[i])
            self.backtracking(nums, path, used, result)
            path.pop()
            used[i] = 0



solution = Solution()
solution.permute(nums=[1,2,3])
