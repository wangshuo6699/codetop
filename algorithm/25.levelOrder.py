# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque

        result = []
        queue = deque([root])
        while queue:
            vector = []
            n = len(queue)
            for _ in range(n):
                cur = queue.popleft()
                vector.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(vector)
        return result

node1 = TreeNode(15)
node2 = TreeNode(7)
node3 = TreeNode(20, node1, node2)
node4 = TreeNode(9)
root  = TreeNode(3, node4, node3)

solution = Solution()
res = solution.levelOrder(root)
print(res)
