def resolve():
    '''
    code here
    '''
    K = int(input())

    is_found = False
    
    def prime_factorize(n):
        a = []
        while n % 2 == 0:
            a.append(2)
            n //= 2
        f = 3
        while f * f <= n:
            if n % f == 0:
                a.append(f)
                n //= f
            else:
                f += 2
        if n != 1:
            a.append(n)
        return a

    for i in range(15):
        print(int('7'*(i+1)))
        print(prime_factorize(int('7'*(i+1))))

if __name__ == "__main__":
    resolve()
