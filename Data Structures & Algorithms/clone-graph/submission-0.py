class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        old_to_new = {}

        def dfs(node):

            if node in old_to_new:
                return old_to_new[node]

            clone = Node(node.val)
            old_to_new[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)