"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        seen = {}

        def dupe(node):
            if node in seen:
                return seen[node]
            if not node:
                return
            c_node = Node(node.val)
            seen[node] = c_node
            c_node.next = dupe(node.next)
            c_node.random = dupe(node.random)
            return c_node
        
        return dupe(head)
        