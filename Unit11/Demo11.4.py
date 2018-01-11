# -*- coding=utf-8 -*-
def firstNonBlank():
    pass

def firstLast(webpage):
    f = open(webpage)
    line = f.readlines()
    f.close()
    print firstNon
    pass

def download(url='http://www.', process=firstLast):
    try:
        retval = urlretrieve(url)[0]
    except IOError:
        retval = none
    if retval:
        process(retval)
    pass

if __name__ == '__main__':
    download()
