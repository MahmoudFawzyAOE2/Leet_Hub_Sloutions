# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        
        cur = dummy =  ListNode() 
        add = 0
        
        while l1 != None or l2 != None or add != 0:
            
            if l1 != None :
                add += l1.val
                l1 = l1.next
            
            if l2 != None :
                add += l2.val
                l2 = l2.next
            
            cur.next = ListNode(val = add if add<10 else add-10 )
            cur = cur.next   
            
            #print('cur', cur)
            #print('dummy', dummy)
            #print()
            
            add = 0 if add<10 else 1   
        return dummy.next      