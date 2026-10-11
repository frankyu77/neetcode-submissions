
'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

valid tree
    - no cycles
    - can reach every node

given any random node:
    - call bfs from that node and check that it can visit every single node in the graph
    - bfs has a visited set so you dont visited nodes you already seen
        - we can have our visited set check for cycles
        - since undirected edges, we can go back to parent
            - need a way to track the parents????
                - use parent set

[[0,1],[0,2],[0,3],[1,4],[2,3]]
graph = {
    0: [1, 2, 3],
    1: [0, 4],
    2: [0, 3],
    3: [0, 2]
    4: [1]
}
visited = {0, 1, 2, 3, 4}
queue = [(3, 0), (4, 1)]

(2, 0)
'''
from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = set()
        queue = deque()
        
        for edge in edges:
            u, v = edge[0], edge[1]
            graph[u].append(v)
            graph[v].append(u)
        
        visited.add(0)
        queue.append((0, -1))

        while queue:
            node, parent = queue.pop()
            for neighbour in graph[node]:
                if neighbour == parent:
                    continue
                if neighbour in visited:
                    return False
                visited.add(neighbour)
                queue.append((neighbour, node))
        return len(visited) == n 







        