# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        
        while head != None :
            one = head.val
            head = head.next
            
            if head != None :
                two = head.val
                head = head.next
            
                cur.next = ListNode(val = two)
                cur = cur.next
            
            cur.next = ListNode(val = one)
            cur = cur.next
     
        return dummy.next