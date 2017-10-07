fib_dict = {}

def fib(n,l):

    fib_list = l
    fib_list.append(n)
    if n == 0 or n == 1:
        return n
    else:
        if n in fib_dict:
            return fib_dict[n]
        else:
            value = fib (n - 1, l) + fib(n - 2 , l)
            fib_dict[n] = value
            return value
