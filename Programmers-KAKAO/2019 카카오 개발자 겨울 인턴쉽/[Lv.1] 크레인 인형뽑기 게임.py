def solution(board, moves):
    n = len(board)

    dolls = [[] for _ in range(n)]
    for i in range(n)[::-1]:
        for j in range(n):
            doll = board[i][j]
            if doll > 0:
                dolls[j].append(doll)

    picked = []
    answer = 0

    for move in moves:
        move -= 1
        if dolls[move]:
            doll = dolls[move].pop()
            if picked and picked[-1] == doll:
                picked.pop()
                answer += 2
            else:
                picked.append(doll)

    return answer
