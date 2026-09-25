class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        adj = [[] for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            adj[prerequisite].append(course)

        visited = set()
        path = set()

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

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True