'''
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.
    - course a depends on course b


adjacency_list = {course : [all courses that depend on this course]}
indegrees = [0] * numCourses

- go through all courses with indegree 0
- mark them as taken, and decrease indegrees of all courses that depend on thsi course
    - any course that has indegree 0 gets will be visited next
    - gets added to the queue

- return true if all elements in indegree is 0, else false
'''
from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        aj = defaultdict(list)
        indegrees = [0] * numCourses
        can_take = deque()

        for pr in prerequisites:
            a, b = pr[0], pr[1]
            aj[b].append(a)
            indegrees[a] += 1

        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                can_take.append(i)

        while can_take:
            course = can_take.popleft()
            for nc in aj[course]:
                indegrees[nc] -= 1
                if indegrees[nc] == 0:
                    can_take.append(nc)

        for indegree in indegrees:
            if indegree != 0:
                return False
        return True





