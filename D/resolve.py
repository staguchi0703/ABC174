def resolve():
    '''
    code here
    '''
    N = int(input())
    stones = input()

    w = []
    r = []

    for i in range(N):
        if stones[i] == 'W':
            w.append(i)
        else:
            r.append(i)

    if len(w) != 0 and len(r) != 0:
        res = 0
        for i, val in enumerate(w):
            if val <= r[-1*(i+1)]:
                res += 1
            else:
                break
        print(res)
    else:
        print(0)

if __name__ == "__main__":
    resolve()
