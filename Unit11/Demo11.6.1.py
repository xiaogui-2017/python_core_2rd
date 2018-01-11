# -*- coding=utf-8 -*-
def tupleVarArgs(arg1, arg2='defaultB', *args):
    'display regular args and non-keyword variable args'
    print 'fromal1 arg1:', arg1
    print 'fromal1 arg2:', arg2
    for index, eachXtrArg in enumerate(args):
        print 'another', index + 1, eachXtrArg


tupleVarArgs('abd')
print '\n'
tupleVarArgs(23, 4.56)
print '\n'
tupleVarArgs('abc', 123, 'xyz', 454313.1341)

