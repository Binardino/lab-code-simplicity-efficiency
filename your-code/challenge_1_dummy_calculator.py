#!/usr/bin/env python
# coding: utf-8

# In[12]:
"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.
"""

number_str = ['zero', 'one', 'two', 'three', 'four', 'five']
operator_str = ['plus', 'minus']

number_dico = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5}

print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')


a = (input("'Please choose your first number (zero to five): "))
c = input('Please choose your second number (zero to five): ')
while a not in number_dico.keys() and c not in number_dico.keys():
    a = input('wait a minute !! a & c must be equal to a number between zero & five, no more, no less')
    c = input('wait a minute !! a & c must be equal to a number between zero & five, no more, no less')

a = number_dico.get(a)
c = number_dico.get(c)
    
b = (input('What do you want to do? plus or minus: '))
while b not in operator_str:
    b = input('wait a minute !! a & c must be a plus or a minus, no more, no less')

if b == 'plus' :
    result = a+c
else:
    result = a-c

print(f'{a} {b} {c} equals to {result}')


# In[ ]:




