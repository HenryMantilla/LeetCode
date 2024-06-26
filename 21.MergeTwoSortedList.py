from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:     
        head = current = ListNode(0)
        while list1 and list2:
            if(list1.val < list2.val):
                current.next, list1 = list1, list1.next
            else:
                current.next, list2 = list2, list2.next
            current = current.next
        current.next = list1 or list2
        return head.next


list1, list2 = ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))
solution = Solution()
print(solution.mergeTwoLists(list1, list2))