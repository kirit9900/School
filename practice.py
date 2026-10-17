'''def pl(a,b):
    return a+b
def ms(a,b):
    return a-b
def um(a,b):
    return a*b
def d(a,b):
    return a/b
a,oper,b = map(str,input().split())
a, b = int(a), int(b)
c = {'+':pl,"-":ms,"*":um,"/":d}
print(c[oper](a, b))'''
from test import *
def test():
    assert test_palidrom('Пап') == False





