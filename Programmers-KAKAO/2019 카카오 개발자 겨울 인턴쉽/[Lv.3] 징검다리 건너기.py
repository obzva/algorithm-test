import collections


def solution(stones, k):
    # SEGMENT TREE - TIME LIMIT EXCEED

    # size = len(stones)
    # stree = [-sys.maxsize] * (2 * size)
    #
    # for i in range(size):
    #     stree[i + size] = stones[i]
    # for i in range(size - 1, 0, -1):
    #     stree[i] = max(stree[2 * i], stree[2 * i + 1])
    #
    # def query(left: int, right: int):
    #     result = -sys.maxsize
    #     left += size
    #     right += size
    #     while left <= right:
    #         if left % 2 == 1:
    #             result = max(result, stree[left])
    #             left += 1
    #         if right % 2 == 0:
    #             result = max(result, stree[right])
    #             right -= 1
    #         left //= 2
    #         right //= 2
    #     return result
    #
    # answer = sys.maxsize
    # for i in range(size - k + 1):
    #     answer = min(answer, query(i, i + k - 1))
    # return answer

    # MIN SLIDING WINDOW USING DEQUE

    id_q = collections.deque()

    def dq_operate(idx: int):
        if id_q and id_q[0] == idx - k:
            id_q.popleft()
        while id_q and stones[id_q[-1]] < stones[idx]:
            id_q.pop()
        id_q.append(idx)

    for i in range(k):
        dq_operate(i)

    answer = stones[id_q[0]]

    for i in range(k, len(stones)):
        dq_operate(i)
        answer = min(answer, stones[id_q[0]])

    return answer
