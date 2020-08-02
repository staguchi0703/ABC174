from heapq import heapify


def resolve():
    '''
    code here
    '''
    import heapq
    N, K = [int(item) for item in input().split()]
    As = [-1 * int(item) for item in input().split()]

    heapq.heapify(As)

    for _ in range(K):
        temp = heapq.heappop(As)
        temp = -1*temp
        nest_num = heapq.heappop(As)
        print(temp, nest_num)

        add_num = temp +nest_num
        heapq.heappush(As, -1*add_num )
        heapq.heappush(As, nest_num)

    # print(As)
    print(-1*heapq.heappop(As))

if __name__ == "__main__":
    resolve()
