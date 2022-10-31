# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:


class Solution:

    def findCelebrity(self, n: int) -> int:

        # BRUTE FORCE
        # def is_celebrity(i):
        #     for j in range(n):
        #         if j == i:
        #             continue
        #         if knows(i, j) or not knows(j, i):
        #             return False
        #     return True
        # for i in range(n):
        #     if is_celebrity(i):
        #         return i
        # return -1

        # LOGICAL DEDUCTION
        # celeb_cand = 0
        # for i in range(1, n):
        #     if knows(celeb_cand, i):
        #         celeb_cand = i
        # if any(knows(celeb_cand, i) for i in range(celeb_cand)):
        #     return -1
        # if any(not knows(i, celeb_cand) for i in range(n)):
        #     return -1
        # return celeb_cand

        # LOGICAL DEDUCTION WITH CACHING
        # cache = dict()
        # celeb_cand = 0
        # for i in range(1, n):
        #     if knows(celeb_cand, i):
        #         cache[(celeb_cand, i)] = True
        #         celeb_cand = i
        #     else:
        #         cache[(celeb_cand, i)] = False
        #
        # def is_celebrity(i):
        #     for j in range(n):
        #         if j == i:
        #             continue
        #         if (i, j) in cache:
        #             if cache[(i, j)]:
        #                 return False
        #         else:
        #             if knows(i, j):
        #                 return False
        #
        #         if (j, i) in cache:
        #             if not cache[(j, i)]:
        #                 return False
        #         else:
        #             if not knows(j, i):
        #                 return False
        #     return True
        #
        # return celeb_cand if is_celebrity(celeb_cand) else -1

        # LOGICAL DEDUCTION WITH CACHING USING LRUCACHE DECORATOR
        @functools.lru_cache(maxsize=None)
        def cached_knows(i: int, j: int) -> bool:
            return knows(i, j)

        celeb_cand = 0
        for i in range(1, n):
            if cached_knows(celeb_cand, i):
                celeb_cand = i
        if any(cached_knows(celeb_cand, i) for i in range(celeb_cand)):
            return -1
        if any(not cached_knows(i, celeb_cand) for i in range(n)):
            return -1
        return celeb_cand

        # JAVA SOLUTION
#         / *The
#         knows
#         API is defined in the
#         parent
#
#         class Relation.
#
#         boolean
#         knows(int
#         a, int
#         b); * /
#
#         public
#
#         class Solution extends Relation {
#
#         private int numberOfPeople;
#         private Map < Pair < Integer, Integer >, Boolean > cache = new HashMap <> ();
#
#         @ Override
#         public boolean knows(int a, int b) {
#         if (!cache.containsKey(new Pair(a, b))) {
#         cache.put(new Pair(a, b), super.knows(a, b));
#         }
#
#         return cache.get(new
#         Pair(a, b));
#         }
#
#         public
#         int
#         findCelebrity(int
#         n) {
#         int
#         celebrityCandidate = 0;
#         for (int i = 0; i < n; i++) {
#         if (knows(celebrityCandidate, i)) {
#         celebrityCandidate = i;
#         }
#         }
#         for (int i = 0; i < celebrityCandidate; i++) {
#         if (knows(celebrityCandidate, i)) {
#         return -1;
#         }
#         }
#         for (int i = 0; i < n; i++) {
#         if (!knows(i, celebrityCandidate)) {
#         return -1;
#
#     }
#     }
#     return celebrityCandidate;
#
# }
# }
