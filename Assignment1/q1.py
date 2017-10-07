def gcd(a,b):
    divisor = [ ]
    if a > b:
        for x in range(1, a+1, 1):
            if ((a % x == 0 ) and (b % x == 0)):
                divisor.append(x)
        if(divisor.__len__() == 0):
            print "no divisor found"
            return divisor

        else:
            greatest_divisor = max(divisor)
            return greatest_divisor

    else:
        for x in range(1, b+1, 1):
            if ((a % x == 0) and (b % x == 0)):
                divisor.append(x)
        if (divisor.__len__() == 0):
                print "no divisor found"
                return divisor

        else:
            greatest_divisor = max(divisor)
            return greatest_divisor
