T = int(input())
    N = []
    teamG = []
    opponent = []
    for i in range(T):
        N.append(int(input()))
        _teamg = [int(x) for x in input().split()]
        _teamg = sorted(_teamg)
        _oppo = [int(x) for x in input().split()]
        _oppo = sorted(_oppo)
        teamG.append(_teamg)
        opponent.append(_oppo)
    for _ in range(T):
        win = 0
        j = 0
        for i in range(N[_]):
            if teamG[_][i]>opponent[_][j]:
                win += 1
                j += 1
        print(win)
