def pal():
    print (" Insert a word or sentence")
    word= input()
    if ' ' in word:
        word= word.replace( ' ', '')
    if '.' in word:
        word= word.replace( '.', '')
    print(word)
    forward = []
    backwards= []
    for x in word:
        forward.append(x)

    for y in reversed(word):
       backwards.append(y) 
    if forward == backwards:
        print('It is a palindrome!!')
        return True
    else:
        print('It is not a palindrome!!')
        return False
pal()

