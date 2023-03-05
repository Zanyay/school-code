#sentence = 'ottawa ontario 647 687 7903'

#number = ''
#for i in sentence:
    #if i.isdigit():
        #number += i

#print(number)

def count_vowels(strang):
    numb = 0
    for i in strang:
        if i in 'aeiouAEIOU':
            numb+=1
    return numb
                
