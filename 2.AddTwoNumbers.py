from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tmp1 = []
        tmp2 = []
        while l1:
            tmp1.append(l1.val)
            l1 = l1.next
        while l2:
            tmp2.append(l2.val)
            l2 = l2.next
        tmp1 = tmp1[::-1]
        tmp2 = tmp2[::-1]

        int_tmp1 = int("".join(str(x) for x in tmp1))
        int_tmp2 = int("".join(str(x) for x in tmp2))

        add = str(int_tmp1 + int_tmp2)
        head = ListNode(int(add[-1]))
        linkedList = head
        
        for i in add[-2::-1]:
            linkedList.next = ListNode(int(i))
            linkedList = linkedList.next
            
        tmp3 = []
        while head:
            tmp3.append(head.val)
            head = head.next
        print(tmp3)


l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

solution = Solution()
solution.addTwoNumbers(l1, l2)