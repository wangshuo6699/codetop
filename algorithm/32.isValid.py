class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        queue = []
        symbol_dict = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in symbol_dict:
                if not queue:
                    return False
                else:
                    if queue[-1]==symbol_dict[char]:
                        queue.pop()
                    else:
                        return False
            else:
                queue.append(char)
        if not queue:
            return True
        else:
            return False

solution = Solution()
res = solution.isValid("()[]{}")
print(res)
