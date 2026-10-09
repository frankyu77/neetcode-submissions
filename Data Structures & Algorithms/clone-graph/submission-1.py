'''
Given a node in a connected undirected graph, return a deep copy of the graph.
    - return a start of the graph that has the same format

Each node in the graph contains an integer value and a list of its neighbors.

The graph is shown in the test cases as an adjacency list.

For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph. The index of each node within the adjacency list is the same as the nodes value (1-indexed).

The input node will always be the first node in the graph and have 1 as the value.

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}
        def dfs(node):
            if not node:
                return None
            
            if node in clones:
                return clones[node]
            
            copy = Node(node.val)
            clones[node] = copy
            for neighbour in node.neighbors:
                copy.neighbors.append(dfs(neighbour))
            return copy
        return dfs(node)
