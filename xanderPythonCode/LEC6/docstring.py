def find_numb(strang):
    '''takes a string and finds a number inside the string,
    turns it into int'''

    s = 0
    numb = '1234567890'
    for char in strang:
        for num in numb:
            if char == num:
                s = int(char)
                return s
                break
    
