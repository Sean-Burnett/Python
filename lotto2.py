import os,sys

a = []

def pickThree():
    
    while True:
        
        b = input("Input the first digit of the most recent pick three number:")
        if b not in [0,1,2,3,4,5,6,7,8,9]:
            print "Unacceptable input. Please input numerical values one at a time."
            pickThree()
        else:
            a.append(b)
        
        c = input("Input the second digit of the most recent pick three number:")
        if c not in [0,1,2,3,4,5,6,7,8,9]:
            print "Unacceptable input. Please input numerical values one at a time."
            pickThree()
        else:
            a.append(c)
        
        d = input("Input the third digit of the most recent pick three number:")
        if d not in [0,1,2,3,4,5,6,7,8,9]:
            print "Unacceptable input. Please input numerical values one at a time."
            pickThree()
        else:
            a.append(d)
        
        break
    
pickThree()

print a
    


