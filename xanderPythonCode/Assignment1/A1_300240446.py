import math

def series_sum():

  '''takes a non-negative integer and returns the sum of the series'''
    
  n = int(input("please input a non-negative integer: "))
  if n == 0:
      return 1000
  #the check for n==0 is because you get an error for dividing by 0 otherwise
    
  elif n>0:
    total = 0
    for num in range(n):
        num += 1
        #this is to avoid starting from 0 and dividing by 0
        subtotal = num*num
        subtotal = 1/subtotal
        total = total + subtotal
    total += 1000
    return total
  else:
    return None



def encrypt(s):
        '''str -> str
encrypts a string by inverting it then spellinga new string from the outside inwards'''
        s = s[::-1]
        l = len(s)
        l = int(l/2)
        a = s[:l]
        b = s[l:]
        b = b[::-1]
        message = ''
        if len(s)==1:
            return s
        elif len(s)%2==0:
            for i in range(l):
                message += a[i]
                message += b[i]
        else:
            for i in range(l):
                message += a[i]
                message += b[i]
            message += s[l]
        return  message

def month_apart(m1,d1,m2,d2):
    '''[int,int,int,int] -> boolean
takes two dates (month and day) and determines if they're a month apart in boolean'''

    if m1 < m2:
        if (m1 + 1) != m2:
            return True
        elif d1 <= d2:
            return True
        else:
            return False
    elif m1 > m2:
        if (m1 - 1) != m2:
            return True
        elif d1 >= d2:
            return True
        else:
            return False
    else:
        return False


def count_even_digits(a):
    '''int -> int
takes any number and will out put the amount of even digits'''
    a = str(a)
    c = 0
    for i in a:
        i = int(i)
        if i == 0 or i==2 or i==4 or i==6 or i==8:
            c = c+1
    return c
            

