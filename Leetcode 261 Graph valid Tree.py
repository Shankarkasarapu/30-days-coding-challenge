from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:  # condition for tree
            return False
        
        # Build adjacency list
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        
        def dfs(node, parent):
            if node in visited:
                return False  # cycle detected
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:  # don’t go back to parent
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        # Start DFS from node 0
        return dfs(0, -1) and len(visited) == n
