import sys, os

a = []
b=98
c=98
d=98
e=98
f=98
g=98
def pickThree():
    while True:
        try:
            b = input("Input the first number of the last mega million number:")
            if b not in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75]:
                print"Not valid input. Input the first number."
                pass
            else:
                a.append(b)
                break
        except:
            print"Not valid input. Input the first number."
            pass
    while True:
        try:
            c = input("Input the second number of the last mega million number:")
            if c not in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75]:
                print"Not valid input. Input the second number."
                pass
            else:
                if c == b:
                    print "You've already entered this number"
                    pass
                else:
                    a.append(c)
                    break
        except:
            print"Not valid input. Input the second number."
            pass
    while True:
        try:
            d = input("Input the third number of the last mega million number:")
            if d not in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75]:
                print"Not valid input. Input the third number."
                pass
            else:
                if d == c or d == b:
                    print "You've already entered this number"
                    pass
                else:
                    a.append(d)
                    break
        except:
            print"Not valid input. Input the third number."
            pass
    while True:
        try:
            e = input("Input the fourth number of the last mega million number:")
            if e not in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75]:
                print"Not valid input. Input the fourth number."
                pass
            else:
                if e == d or e == c or e == b:
                    print "You've already entered this number"
                    pass
                else:
                    a.append(e)
                    break
        except:
            print"Not valid input. Input the fourth number."
    while True:
        try:
            f = input("Input the fifth number of the last mega million number:")
            if f not in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75]:
                print"Not valid input. Input the fifth number."
                pass
            else:
                if f == e or f == d or f == c or f == b:
                    print "You've already entered this number"
                    pass
                else:
                    a.append(f)
                    break
        except:
            print"Not valid input. Input the fifth number."
    while True:
        try:
            g = input("Input the megaball number of the last mega million number:")
            if g not in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
                print"Not valid input. Input the megaball number."
                pass
            else:
                a.append(g)
                break
        except:
            print"Not valid input. Input the megaball number."
    u = a[0]
    v = a[1]
    w = a[2]
    x = a[3]
    y = a[4]
    z = a[5]
    

    print "%d,%d,%d,%d,%d,%d"%(((round(u + (3.141592653**.5)))%75),((round(v + (3.141592653**.5)))%75),((round(w + (3.141592653**.5)))%75),((round(x + (3.141592653**.5)))%75),((round(y + (3.141592653**.5)))%75),((round(z + (3.141592653**.5)))%15))
    print "%d,%d,%d,%d,%d,%d"%(((round(u + (3.141592653)))%75),((round(v + (3.141592653)))%75),((round(w + (3.141592653)))%75),((round(x + (3.141592653)))%75),((round(y + (3.141592653)))%75),((round(z + (3.141592653)))%15))
    print "%d,%d,%d,%d,%d,%d"%(((round(u + (3.141592653**2)))%75),((round(v + (3.141592653**2)))%75),((round(w + (3.141592653**2)))%75),((round(x + (3.141592653**2)))%75),((round(y + (3.141592653**2)))%75),((round(z + (3.141592653**2)))%15))
    raw_input("done!!")

pickThree()
