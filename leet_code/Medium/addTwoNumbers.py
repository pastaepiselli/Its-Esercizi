# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

class Solution:
    def addTwoNumbers(self, l1: list[int], l2: list[int]) -> list[int]:

        a: int = 0
        b: int = 0
        zero = 0
        for i in l1:
            a += (i + zero)
            zero *= 10
        
        zero = 0
        for j in l1:
            b += (j + zero)
            zero *= 10
        
        s = a + b
        s = str(s)

        new_list = []
        for h in s[::-1]:
            new_list.append(h)


        return new_list

        
s = Solution()
a = s.addTwoNumbers([2,3,4], [5,6,4])
print(a)

