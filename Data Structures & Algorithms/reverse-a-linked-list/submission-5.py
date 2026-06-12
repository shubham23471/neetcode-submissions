# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


## APPROCH - 1 BRUTE FORCE 
## STEPS 
## 1) traverse the LL -> collect the items into a new python list [O(n)]
## 2) Reverse that list [O(n)] + extra space
## 3) Create a new LL from those reversed items [O(n)] 

# [0,1,2,3]
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: 
            None
        
        prev = None
        current = head
        while current != None:
            next = current.next  
            current.next = prev

            prev = current  # frwd prev 
            current = next # frd current value 
        
        return prev

