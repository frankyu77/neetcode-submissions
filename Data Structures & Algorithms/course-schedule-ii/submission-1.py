from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        aj = defaultdict(list)
        indegrees = [0] * numCourses
        can_take = deque()
        sol = []

        for pr in prerequisites:
            a, b = pr[0], pr[1]
            aj[b].append(a)
            indegrees[a] += 1

        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                can_take.append(i)

        while can_take:
            course = can_take.popleft()
            sol.append(course)
            for nc in aj[course]:
                indegrees[nc] -= 1
                if indegrees[nc] == 0:
                    can_take.append(nc)

        for indegree in indegrees:
            if indegree != 0:
                return []
        return sol





