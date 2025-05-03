def solve(board=[], row=0):
    if row == 8:
        print(board)
        return
    for col in range(8):
        if all(col != c and abs(row - r) != abs(col - c) for r, c in enumerate(board)):
            solve(board + [col], row + 1)

solve()
