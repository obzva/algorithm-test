import sys

n = int(input())

numbs = sorted(list(map(int, sys.stdin.readline().split())))

x = int(input())

start = 0
end = n - 1
res = 0

while start < end:
    tmp_sum = numbs[start] + numbs[end]
    if tmp_sum == x:
        start += 1
        end -= 1
        res += 1
    elif tmp_sum < x:
        start += 1
    else:
        end -= 1

print(res)
