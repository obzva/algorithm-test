import heapq

a = b = []

print(id(a))
print(id(b))

heapq.heappush(a, 1)
heapq.heappush(a, 3)
heapq.heappush(a, 2)
heapq.heappush(a, 6)

print(a)
print(b)
