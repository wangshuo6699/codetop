class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if (len(nums1)+len(nums2))%2==1:
            return self.findMedian(nums1, nums2, (len(nums1)+len(nums2)+1)//2)
        else:
            mid = (len(nums1)+len(nums2))//2
            return (self.findMedian(nums1, nums2, mid)+self.findMedian(nums1, nums2, mid+1))/2
    
    def findMedian(self, nums1, nums2, k):
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1
        index1, index2 = 0, 0
        m, n = len(nums1), len(nums2)
        while True:
            if index1==m:
                return nums2[index2+k-1]
            if index2==n:
                return nums1[index1+k-1]
            if k==1:
                return min(nums1[index1], nums2[index2])

            newIndex1 = min(index1 + k // 2 - 1, m - 1)
            newIndex2 = min(index2 + k // 2 - 1, n - 1)
            pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
            if pivot1 <= pivot2:
                k -= newIndex1 - index1 + 1
                index1 = newIndex1 + 1
            else:
                k -= newIndex2 - index2 + 1
                index2 = newIndex2 + 1
    
solution = Solution()
res = solution.findMedianSortedArrays(nums1 = [1,3], nums2 = [2,4])
print(res)
