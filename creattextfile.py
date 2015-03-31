import time as t
from os import path

def creatFile(dest):
    '''
    The script creates a text file at the passed in location, name
    based on date
    '''
    date = t.localtime(t.time())
    ##FileName = Month Day Year
    name = '%d_%d_%d.txt'%(date[1],date[2],(date[0]%100))
    if not(pathisfile(dest+name)):
        f=open(dest+name,'w')
        f.write('\n'*30)
        f.close()
        
if __name__ == '__main__':
    destination = 'C:\\Users\
\\NaesCB\\Desktop\\pythonstuff\\'
    createFile(destination)
    raw_input("done!!")
