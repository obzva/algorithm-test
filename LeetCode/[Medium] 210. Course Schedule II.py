import collections
from typing import *


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashmap = collections.defaultdict(list)
        for course, prerequisite in prerequisites:
            hashmap[course].append(prerequisite)

        traced = set()
        visited = list()
        num_course_set = set(range(numCourses))

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
            visited.append(i)
            num_course_set.remove(i)
            return True

        for course in hashmap_list:
            if not dfs(course):
                return []
        return visited + list(num_course_set)
