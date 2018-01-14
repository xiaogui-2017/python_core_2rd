# -*- coding=utf-8 -*-
"""变量作用域， 名称空间"""

j, k = 1, 2


def pro1():
    j, k = 3, 4
    print "j==%d and k==%d" % (j, k)
    k = 5


def pro2():
    j = 6
    pro1()
    print "j==%d and k==%d" % (j, k)


k = 7
pro1()
print "j==%d and k==%d" % (j, k)

j = 8
pro2()
print "j==%d and k==%d" % (j, k)
