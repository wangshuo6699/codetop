class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0]<=nums[mid]:
                if target>=nums[0] and target<nums[mid]:
                    r = mid -1
                else:
                    l = mid + 1
            else:
                if target>nums[mid] and target<=nums[-1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


solution = Solution()
res = solution.search(nums=[3, 1], target = 1)
print(res)
