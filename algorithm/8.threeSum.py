class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i]>0:
                return []
            if i>0 and nums[i]==nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left<right:
                if nums[i]+nums[left]+nums[right]<0:
                    left += 1
                elif nums[i]+nums[left]+nums[right]>0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while right>left and nums[right]==nums[right-1]:
                        right-=1
                    left += 1
                    right -= 1
        return result
                    
solution = Solution()
solution.threeSum(nums = [-1,0,1,2,-1,-4])
