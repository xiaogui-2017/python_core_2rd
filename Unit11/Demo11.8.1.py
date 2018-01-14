# -*- coding=utf-8 -*-
all_par = 100


def foo():
    """如果赋予局部变量之前，你在函数中（为了防止这个全局变量）使用了这样名字，你将会得到一个异常，NAMEERROR/Unbound-LocalError"""
    print all_par
    all_par = 10

foo()
