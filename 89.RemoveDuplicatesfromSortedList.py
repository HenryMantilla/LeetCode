# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head

        if head == None or head.next == None:
            return head
        
        while pointer and pointer.next:
            if pointer.val == pointer.next.val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next 

        return head
    

a = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
solution = Solution()
print(solution.deleteDuplicates(a))