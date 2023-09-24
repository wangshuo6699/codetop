class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if not m:
            nums1[:] = nums2
            return nums1
        elif not n:
            return nums1
        else:
            j = len(nums2)-1
            nums2 = nums2[:n]
            tmp_list = nums1[:m]
            for i in range(len(tmp_list)-1, -1, -1):
                while j>=0 and nums2[j]>=tmp_list[i]:
                    tmp_list.insert(i+1, nums2.pop(j))
                    j -= 1
            nums1[:] = nums2+tmp_list

solution = Solution()
res = solution.merge(nums1 = [2,0], m = 1, nums2 = [1], n = 1)
print(res)
