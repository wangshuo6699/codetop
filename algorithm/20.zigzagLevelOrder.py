# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque

        if not root:
            return root

        result = []
        left_flag = True
        queue = deque([root])
        while queue:
            vector = []
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                vector.append(node.val)
            if not left_flag:
                vector = list(reversed(vector))
            left_flag = not left_flag
            result.append(vector)
        return result


node1 = TreeNode(15)
node2 = TreeNode(7)
node3 = TreeNode(20, node1, node2)
node4 = TreeNode(9)
root  = TreeNode(3, node4, node3)

solution = Solution()
res = solution.zigzagLevelOrder(root)
print(res)
