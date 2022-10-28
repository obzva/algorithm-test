import collections
from typing import *


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # MY SOLUTION - TIME LIMIT EXCEED
        # if not prerequisites:
        #     return True
        #
        # hashmap = dict()
        # for course, pre_req_course in prerequisites:
        #     hashmap[course] = pre_req_course
        #
        # for course, pre_req_course in prerequisites:
        #     pres = [course]
        #     while True:
        #         if pre_req_course in pres:
        #             return False
        #         if pre_req_course not in hashmap:
        #             break
        #         course = pre_req_course
        #         pre_req_course = hashmap[course]
        #         pres.append(course)
        # return True

        # PYTHON ALGORITHM INTERVIEW
        hashmap = collections.defaultdict(list)
        for course, prereq in prerequisites:
            hashmap[course].append(prereq)

        traced = set()
        visited = set()

        hashmap_list = list(hashmap)

        def dfs(i):
            if i in traced:
                return False
            if i in visited:
                return True

            traced.add(i)
            for y in hashmap[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
            visited.add(i)
            return True

        for course in hashmap_list:
            if not dfs(course):
                return False
        return True