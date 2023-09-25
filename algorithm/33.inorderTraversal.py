# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        return left+[root.val]+right

node1 = TreeNode(3)
node2 = TreeNode(2, node1)
root  = TreeNode(1, None, node2)

solution = Solution()
res = solution.inorderTraversal(root)
print(res)
