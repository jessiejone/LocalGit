#! /usr/bin/env python
print "sunck is a good man"
#multiple messages
print "Hello World", "I am happy"
'''
12345
57890
'''
"""
abcdef
"""
print (18)
print 10 + 8
print "10 + 8 =", 18

#input get var , age is a string
age=input()
print "age=",age
import keyword
print keyword.kwlist

num1 = int(input ("please input a number"))
num2 = int (input ("please input a number"))
print "num1 + num2 = ", num1 + num2

#var type
print (type(num1))
#address of var
print (id(num1))

num6, num7 = 6, 7

f1 = 1.1
f2 = 2.1
print f1 + f2

#var convert
print (float (1)
print (int ("-123"))
a1 = -10
a2 = abs (a1)
print (a2)

# round for two bits after .
print (round(3.856, 2))

#math library
import math
math.ceil(18.1)
#19
math.floor(18.1)
#18
#(0.3000000000,22.0)
print (math.modf(22.3))

import random
print (random.choice([1,3,5,7,9]))

range(5)
#[0, 1, 2, 3, 4]
#[start] default is 0 stop [step]default is 1
random.randrange(1,100,2)

#[0,1)
random.random()

list = [1,2,3,4,5]
print list
#[1, 2, 3, 4, 5]
 random.shuffle(list)
print list
#[5, 4, 1, 2, 3]
random.uniform(3,9)
#7.946455218389511 real value between 3 and 9
#reverse
print (~5, 5^7, 5<<2)