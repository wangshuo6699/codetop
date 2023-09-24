import copy
import random

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.quickSort(nums, 0, len(nums)-1)
        return nums

    def quickSort(self, nums, l, r):
        if l >= r:             # 递归结束
            return  
        i = copy.deepcopy(l)
        j = copy.deepcopy(r)
        pivot_idx = random.randint(l, r)
        nums[l], nums[pivot_idx] = nums[pivot_idx], nums[l]
        pivot = nums[l]
        while l<r:
            while l<r and pivot<=nums[r]:
                r-=1
            nums[l] = nums[r]
            while l<r and pivot>=nums[l]:
                l+=1
            nums[r] = nums[l]
        nums[l] = pivot
        self.quickSort(nums, i, l-1)
        self.quickSort(nums, l+1, j)


solution = Solution()
res = solution.sortArray(nums = [5,2,9,1,3,6])
print(res)
        