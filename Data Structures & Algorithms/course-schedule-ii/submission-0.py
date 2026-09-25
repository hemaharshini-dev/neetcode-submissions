class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            adj[prerequisite].append(course)

        visited = set()
        path = set()
        result = []

        def dfs(course):
            if course in path:
                return False

            if course in visited:
                return True

            path.add(course)

            for neighbor in adj[course]:
                if not dfs(neighbor):
                    return False

            path.remove(course)
            visited.add(course)
            result.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        result.reverse()
        return result