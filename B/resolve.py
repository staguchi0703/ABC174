def resolve():
    '''
    code here
    '''
    N, D = [int(item) for item in input().split()]
    points = [[int(item) for item in input().split()] for _ in range(N)]

    cnt = 0
    for x, y in points:
        if x**2 + y**2 <= D**2:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    resolve()
