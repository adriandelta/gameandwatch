# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 16:07:28 2024
@author: Adrian H

Update Mon Feb 5 18:42 2024
 - Changed ints to strs for printing without extra spaces
 - Added comments for todo list
 
Update Sun Feb 11 12:56 2024
 - Updated todo list
 - Drafted algo steps
 - Added "math" import and absolute value function

Update Sat Mar 02 16:05 2024
 - Added error message if slope == 0

Update Tue Mar 05 13:06 2024
 - Updated outputs to use f'{var}' format where needed
 - Added message if slope == 0, fixed previous error to mean slope is undefined / line is vert
 - Finished a bunch of todos and moved things around for consolidation
 - Added decision trees
 - Mixed comment formatting for legibility
 - Added pyplot import for eventual graphing shenanigans
"""

import math # for greatest common factor (i'm ignoring abs)
import matplotlib.pyplot #  for graphing the line (eventually)

print("This program will calculate \nthe slope and equation for \na line between two points.")
print() # blank line for spacing

''' get the input data for both points '''

print("Point 1 coordinates:")
x1 = int(input(" -> X:"))
y1 = int(input(" -> Y:"))
print(f'Point 1 = ({x1},{y1})')

print() # blank line for spacing

print("Point 2 coordinates:")
x2 = int(input(" -> X:"))
y2 = int(input(" -> Y:"))
print(f'Point 2 = ({x2},{y2})')

print() # blank line for spacing

''' setting up to calculate m '''

m_dividend = y2 - y1
m_divisor = x2 - x1

# if m = 0 or error, then the equations are y = y1 or x = x1 (respectively)
if m_divisor == 0:
  print("Error: Can not divide by zero. \nThe slope of a vertical line is undefined.")
  print("The equation for the line between points 1 & 2 is")
  print(f' x = {x1}')
  quit() # ends the program
elif m_dividend == 0:
  print("The slope of a horizontal line is 0.")
  print("The equation for the line between points 1 & 2 is")
  print(f' y = {y1}')
  quit() # ends the program
else:
  # no errors

if (m_dividend < 0) and (m_divisor < 0): # if both the numerator & denominator are negative
  m_dividend = 0 - m_dividend # make them both positive for display purposes
  m_divisor = 0 - m_divisor # make them both positive for display purposes
# no else needed

''' reduce fractions ''' 
# if gcd != divisor AND dividend >= divisor, then we can simplify, otherwise leave it as is because it will turn into a whole number

if (math.gcd(m_dividend, m_divisor) != m_divisor) and (m_dividend >= m_divisor):
  m_dividend = m_dividend/(math.gcd(m_dividend, m_divisor)) '''does this need to be declared as int() or is it implied?'''
  m_divisor = m_divisor/(math.gcd(m_dividend, m_divisor))
# no else needed

''' calculating b '''
# y = mx + b, so b = y - mx

b = y1 - (m * x1) # if m is a float here, then b will output as a float

if (b - ( b // 1) ) == 0: # if b is a whole number
  b = int(b) # change type from float to int
# no else needed
  
''' calculate and output the slope (m) and full equation '''

if m_dividend % m_divisor == 0: # if m is a whole number fraction displays are not needed
  m = int(m_dividend / m_divisor) # calculate m as int
  print(f'The slope of the line between points 1 & 2 is {m}.')
  print() # blank line
  print("The equation for the line between points 1 & 2 is")
  if b > 0: # if b is greater than or equal to 0
    print(f' y = {m}x + {b}')
  elif b < 0: # if b is less than 0
    b = 0 - b # make it positive for display purposes
    print(f' y = {m}x - {b_abs}') # use - b instead of + b
  else: # if b == 0 remove it entirely
    print(f' y = {m}x')

else: # m is not a whole number
  m = float(f'{(m_dividend) / (m_divisor):.2f}') # calculate m as float
  print(f'The slope of the line between points 1 & 2 is {m}, or {m_dividend}/{m_divisor}.')
  print() # blank line
  print("The equation for the line between points 1 & 2 is")
  if b > 0: # if b is greater than or equal to 0
    print(f' y = {m}x + {b}')
    print("or")  
    print(f' y = ({m_dividend}/{m_divisor})x + {b}')
  elif b < 0: # if b is less than 0
    b = 0 - b # make it positive for display purposes
    print(f' y = {m}x - {b_abs}') # use - b instead of + b
    print("or")
    print(f' y = ({m_dividend}/{m_divisor})x - {b}')
  else: # if b == 0 remove it entirely
    print(f' y = {m}x')
    print("or")
    print(f' y = ({m_dividend}/{m_divisor})x')


# todo: graph (and table?)
''' 
  mathplotlib.pyplot stuff goes here
'''


# end program
