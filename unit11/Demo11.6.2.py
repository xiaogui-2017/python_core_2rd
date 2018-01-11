# -*- coding=utf-8 -*-
def tupleVarArgs(arg1, arg2='defaultB', *args, **kwargs):
    'display regular args and non-keyword variable args'
    print 'fromal1 arg1:', arg1
    print 'fromal1 arg2:', arg2
    for index, eachXtrArg in enumerate(args):
        print 'another', index + 1, eachXtrArg
    for kw in kwargs.keys():
        print kw

tupleVarArgs(30, a=90, b=80)

