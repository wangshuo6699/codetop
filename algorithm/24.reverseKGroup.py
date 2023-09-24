# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkList(object):
    def __init__(self):
        # 先初始化一个头节点，为None
        self.head = None

    # 链表初始化函数, 方法类似于尾插
    def initList(self, data):
        # 创建头结点
        # 这个节点创建完，包含两部分：是个既包含节点值，也包含节点所链接的下一个节点
        self.head = ListNode(data[0])

        # 初始化p指向头节点
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            # 构建完一个节点，移动到构建完的节点上，继续向后构建节点
            p = p.next

import copy

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        i = 0
        dummy_head = ListNode(None)
        cur = dummy_head
        lists = []
        while head:
            i+=1
            cur.next = head
            head = head.next
            cur = cur.next
            if i%k==0:
                cur.next = None
                lists.append([dummy_head.next, 1])
                dummy_head = ListNode(None)
                cur = dummy_head
        if dummy_head.next:
            lists.append([dummy_head.next, 0])

        dummy_head = ListNode(None)
        cur = dummy_head
        for i in range(len(lists)):
            if lists[i][1]:
                node = self.reverseLinkList(lists[i][0])
                while node:
                    cur.next = node
                    cur = cur.next
                    node = node.next
            else:
                node = lists[i][0]
                while node:
                    cur.next = node
                    cur = cur.next
                    node = node.next
        return dummy_head.next

    def reverseLinkList(self, head):
        pre = None
        cur = head
        while cur:
            tmp_head = cur.next
            cur.next = pre
            pre = cur
            cur = tmp_head
        return pre


l = LinkList()
l.initList([1,2,3,4,5])

solution = Solution()
solution.reverseKGroup(head = l.head, k = 2)
