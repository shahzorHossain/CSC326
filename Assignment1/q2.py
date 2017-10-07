def rotate_word(x, i):
    word = x
    reverseWord = word

    for k in range(1,i+1):

        tempWord = reverseWord
        reverseWord = reverseWord[1:]
        reverseWord += tempWord[0]

    print reverseWord
    return reverseWord
