'''
You have an undirected graph of n nodes labeled from 0 to n - 1. You are given an integer n and an array edges where edges[i] = [aᵢ, bᵢ] indicates that there is an edge between aᵢ and bᵢ in the graph.

Return the number of connected components in the graph.

- for each node from 0 to n-1
    - check if the node has already been visited/processed
        - yes?
            continue
        - no?
            updated num_connected_components
            call BFS on it and update our visited/processed set

n = 5, edges = [[0,1],[1,2],[3,4]]

num_connected_components = 2
visited = {0, 1, 2, 3, 4}
'''

from collections import defaultdict, deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for edge in edges:
            u = edge[0]
            v = edge[1]
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        num_connected_components = 0

        def bfs(node: int):
            nonlocal visited

            queue = deque()
            queue.append(node)
            visited.add(node)

            while queue:
                curr = queue.popleft()
                for neighbour in graph[curr]:
                    if neighbour in visited:
                        continue
                    visited.add(neighbour)
                    queue.append(neighbour)

        for node in range(0, n):
            if node in visited:
                continue
            num_connected_components += 1
            bfs(node)
        return num_connected_components


















