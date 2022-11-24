import sys


def solution(k, room_number):
    # CACHE - TIME LIMIT EXCEED

    # cache = collections.defaultdict(bool)
    # answer = []
    # for i in room_number:
    #     room = i
    #     while room <= k and cache[room]:
    #         room += 1
    #     cache[room] = True
    #     answer.append(room)
    #
    # return answer

    # RECURSIVE

    hashmap = {}
    sys.setrecursionlimit(1000000)

    def room_finder(room_no: int):
        if room_no not in hashmap:
            answer.append(room_no)
            hashmap[room_no] = room_no + 1
            return room_no + 1

        hashmap[room_no] = room_finder(hashmap[room_no])
        return hashmap[room_no]

    answer = []
    for want in room_number:
        room_finder(want)

    return answer
