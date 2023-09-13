# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
      """
      :type node: ListNode
      :rtype: void Do not return anything, modify node in-place instead.
      """
      
      # the code and text above were given in the problem
      # Put the value in the node after the node, which is node.next, into the node
      # Make the .next pointer for the node into the contents of the pointer after the node, which is node.next.next
      node.val = node.next.val
      node.next = node.next.next
