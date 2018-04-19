'''
Created on Apr 12, 2018

@author: HUILINGAlanShen
'''
# _*_ coding: cp-1252 _*_
from random import choice, random
from collections import Counter

student={'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)

if('Rose' in student):
    print('Rose is in the sets')
else:
    print('Rose is not in the set')
    
a=set('abracadabra')
b=set('alacazam')

print (a)
print(a-b)
print(a|b)
print(a&b)
print(a^b)

dict ={}
dict['one']="test one"
dict[2]="test two"
tinydict={'name':'runoob', 'code':1,'site': 'www.runoob.com'}

print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

a=60
b=13
c=0

c=a&b;
print(c)
print(a)

a=-10000000000
b=-10000000000
print(id(a))
print(id(b))
print(a is b)
print(a==b)

a=[1,2,3]
b=a[:]
print(a is b)
print(a[:])

print(choice(range(10)))
random()
para_str="""ddfdfdfdfd
TAB(\t).
also use [\n]
"""
print(para_str) 

num=18.7254
print("the price is %.2f" %num)

a=100000
print("%g" %a)
a=1000000
print("%g" %a)
a=10000000
print("%g" %a)
a=100000.1
print("%g" %a)
a=1.0
print("%g" %a)
a=1.1
print("%g" %a)

num=10
print("%#x" %num)
print(bin(num))
print("%#o" %num)

L=['a','b','c','d','e','f','g']
print(L[::2])

s1="I'm a good student"
s2=s1.partition("good")
s3=s1.partition('abc')

print(s1)
print(s2)
print(s3)

var1="134343dfdfdsdsfdsfwereer34343"
var2="dkdkeei484589432837432skfjdf"

print(Counter(var1))
print(Counter(var2))

a=['a', 'b', 'c']
n=[1,2,3]
x=[a,n]
print(x)

list_2d=[[0 for i in range(5)] for i in range(5)]
list_2d[0].append(3)
list_2d[0].append(5)
list_2d[2].append(7)
print(list_2d)

l=[i for i in range(0,15)]
print(l)
print(l[::2])

list_empty=[None]*10

a,b=0,1
while b<10:
    print(b)
    a,b=b,a+b


for n in range(2,20):
    for x in range(2,n):
        if n%x==0:
            print(n,'=',x,'*',n//x)
            break
    else:
        print(n,'is prime number')




