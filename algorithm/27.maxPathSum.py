# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxNum = float('-inf')
        res = self.traversal(root)
        return self.maxNum

    def traversal(self, root):
        if not root:
            return 0
        left = max(self.traversal(root.left), 0)
        right = max(self.traversal(root.right), 0)
        curPathSum = root.val + left + right
        self.maxNum = max(self.maxNum, curPathSum)
        return root.val+max(left, right)


node1 = TreeNode(15)
node2 = TreeNode(7)
node3 = TreeNode(20, node1, node2)
node4 = TreeNode(9)
root  = TreeNode(-10, node4, node3)

node1 = TreeNode(-1)
root  = TreeNode(2, None, node1)

solution = Solution()
res = solution.maxPathSum(root)
print(res)
