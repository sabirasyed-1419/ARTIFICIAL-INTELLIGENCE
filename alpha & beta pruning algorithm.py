def ab(n, d, a, b, maxP):
    if d == 0 or isinstance(n, int): return n
    if maxP:
        for c in n:
            a = max(a, ab(c, d-1, a, b, False))
            if b <= a: break
        return a
    else:
        for c in n:
            b = min(b, ab(c, d-1, a, b, True))
            if b <= a: break
        return b

tree = [[3,5],[6,9],[1,2]]
print("Best:", ab(tree, 3, -999, 999, True))
