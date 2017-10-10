def isPrime(N):

    if N <= 2 :
        return True

    for i in range(2,N,1):
        if N % i == 0 and N != i:
            return False

    return True

def factorize(N):
    prime_list = []

    num = N
    product = 1

    if num == 1 :
        prime_list.append(num)

    if isPrime(N):
        return []

    for i in range(1, num+1, 1):


        if isPrime(i):
            if num % i == 0:
                prime_list.append(i)

    for j in range(1, prime_list.__len__(),1):
        product *= prime_list[j]

    if product == num:
        return prime_list
    else:
        return []


