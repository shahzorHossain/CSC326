from math import sqrt

def Q(D):
    valueList = []
    for i in D:
        result = int(sqrt((2 * 50 * i)/(30)))
        valueList.append(result)

    return valueList

inputValues = [int(x) for x in raw_input().split(',')]
print Q(inputValues)