def win(b, p):
    w = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),
         (1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(b[i]==b[j]==b[k]==p for i,j,k in w)

def mini(b, turn):
    if win(b, 'O'): return 1
    if win(b, 'X'): return -1
    if ' ' not in b: return 0
    scores = []
    for i in range(9):
        if b[i]==' ':
            b[i]=turn
            scores.append(mini(b, 'X' if turn=='O' else 'O'))
            b[i]=' '
    return max(scores) if turn=='O' else min(scores)

def best(b):
    return max((mini(b[:i] + ['O'] + b[i+1:], 'X'), i)
               for i in range(9) if b[i]==' ')[1]

b = [' '] * 9
while True:
    print(f"{b[0]}|{b[1]}|{b[2]}\n{b[3]}|{b[4]}|{b[5]}\n{b[6]}|{b[7]}|{b[8]}")
    m = int(input("0-8: "))
    if b[m] != ' ': continue
    b[m] = 'X'
    if win(b, 'X'): print("You win!"); break
    if ' ' not in b: print("Draw"); break
    b[best(b)] = 'O'
    if win(b, 'O'): print(f"{b[0]}|{b[1]}|{b[2]}\n{b[3]}|{b[4]}|{b[5]}\n{b[6]}|{b[7]}|{b[8]}\nAI wins!"); break
