class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq

        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap)>k:
                heapq.heappop(heap)
        return heapq.heappop(heap)

solution = Solution()
res = solution.findKthLargest([3,2,3,1,2,4,5,5,6], k = 4)
print(res)
