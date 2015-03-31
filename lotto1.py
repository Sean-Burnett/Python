import sys, os

a = []
b=32
c=32
d=32
def pickThree():
    while True:
        try:
            b = input("Input the first didgit of the last pick three number:")
            if b not in [0,1,2,3,4,5,6,7,8,9]:
                print"Not valid input. Input the first single digit."
                pass
            else:
                a.append(b)
                break
        except:
            print"Not valid input. Input the first single digit."
            pass
    while True:
        try:
            c = input("Input the second didgit of the last pick three number:")
            if c not in [0,1,2,3,4,5,6,7,8,9]:
                print"Not valid input. Input the second single digit."
                pass
            else:
                a.append(c)
                break
        except:
            print"Not valid input. Input the second single digit."
            pass
    while True:
        try:
            d = input("Input the third didgit of the last pick three number:")
            if d not in [0,1,2,3,4,5,6,7,8,9]:
                print"Not valid input. Input the third single digit."
                pass
            else:
                a.append(d)
                break
        except:
            print"Not valid input. Input the third single digit."
            pass
    z = a[0]
    x = a[1]
    y = a[2]

    print "%d,%d,%d"%(((round(z + (3.141592653**.5)))%10),((round(x + (3.141592653**.5)))%10),((round(y + (3.141592653**.5)))%10))
    print "%d,%d,%d"%(((round(z + (3.141592653)))%10),((round(x + (3.141592653)))%10),((round(y + (3.141592653)))%10))
    print "%d,%d,%d"%(((round(z + (3.141592653**2)))%10),((round(x + (3.141592653**2)))%10),((round(y + (3.141592653**2)))%10))
    raw_input("done!!")

pickThree()
