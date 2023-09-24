class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        left, right, up, down = 0, len(matrix[0])-1, 0, len(matrix)-1
        while left<right and up<down:
            for i in range(left, right):
                result.append(matrix[up][i])
            for j in range(up, down):
                result.append(matrix[j][right])
            for i in range(right, left, -1):
                result.append(matrix[down][i])
            for j in range(down, up, -1):
                result.append(matrix[j][left])
            left += 1
            right -= 1
            up += 1
            down -= 1
        if up>down or left>right:
            return result
        if up==down:
            for i in range(left, right+1):
                result.append(matrix[up][i])
            return result
        if left==right:
            for i in range(up, down+1):
                result.append(matrix[i][left])
        return result

solution = Solution()
res = solution.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(res)
