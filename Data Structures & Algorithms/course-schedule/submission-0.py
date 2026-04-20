class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i: [] for i in range(numCourses)}
        for course, preq in prerequisites:
            premap[course].append(preq)
        visit = set()
        def dfs(course):
            if course in visit:
                return False
            if premap[course] == []:
                return True
            visit.add(course)

            for pre in premap[course]:
                if not dfs(pre):
                    return False
            visit.remove(course)
            premap[course] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True