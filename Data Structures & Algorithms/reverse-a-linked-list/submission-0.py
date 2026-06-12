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
        if not head : 
            return None
        
        python_list = [] # 0,1,2,3

        current = head
        while current: 
            python_list.append(current.val)
            current = current.next
        
        # 3, 2, 1, 0 
        python_list.reverse()

        # create a new LL 
        new_head = ListNode(python_list[0])
        current = new_head

        for i in python_list[1:]:
            current.next = ListNode(i)
            current = current.next


        return new_head

            