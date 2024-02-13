# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 16:07:28 2024
@author: Adrian H

Update Mon Feb 5 18:42 2024
 - Changed ints to strs for printing without extra spaces.
 - Added comments for todo list
 
Update Sun Feb 11 12:56 2024
 - Updated todo list
 - Drafted algo steps
 - Added "math" import and absolute value function

"""

# import the "math" module so that we can get absolute value later
import math

print("This program will calculate\nthe slope and equation for\na line between two points.")

print() # blank line for spacing

# get the data for both points
print("Point 1 coordinates:")
x1 = int(input(" -> X:"))
y1 = int(input(" -> Y:"))
print("Point 1 = (" + str(x1) + "," + str(y1) + ")")

print() # blank line for spacing

print("Point 2 coordinates:")
x2 = int(input(" -> X:"))
y2 = int(input(" -> Y:"))
print("Point 2 = (" + str(x2) + "," + str(y2) + ")")

print() # blank line for spacing

# run the calculations

m = float(f'{(y2 - y1) / (x2 - x1):.2f}')
m_dividend = y2 - y1
m_divisor = x2 - x1

# calculate b
# y = mx + b, so b = y - mx

'''
if there are no errors
'''
b = y1 - (m * x1)
'''
otherwise
b = y1
'''


# add an error message if m_divisor is 0
'''
    if m_divisor == 0
    print("Error: Can not divide by zero.")
    print("Slope of line is 0.")
    end program
'''


# other vars

m_int = m_dividend // m_divisor
m_rem = m_dividend % m_divisor

# output the result

print("The slope of the line between points 1 & 2 is", 
      m)
print("or")
print(str(m_dividend) +
      "/" +
      str(m_divisor) +
      ".")

print() # blank line


print("The equation for the line between points 1 & 2 is")
print(" y = " +
      str(m) +
      "x + " +
      str(b)
      )
print("or")
print(" y = (" +
      str(m_dividend) +
      "/" +
      str(m_divisor) +
      ")x + " +
      str(b) +
      ".")

# todo: if b is negative output "- absolute_b" instead of "+ b"
'''
  if b<0
  absolute_b = math.fabs(b)
  # should we make these variables regardless of whether or not we are using them?
'''

# todo: if both m_dividend and m_divisor are negative, output absolute val
'''
  if m_dividend < 0
  absolute_m_dend = math.fabs(m_dividend)
  absolute_m_dsor = math.fabs(m_divisor)
'''

# todo: if m and/or b are whole numbers, output them as whole numbers
'''
if m_dividend % m_divisor == 0, 
then print m_int not m
 # see if b is a whole number
then print m_int and b_int
'''

# todo: if m is a whole number, do not print the 2nd equation or slope

''' 
  # how to test if m is a whole number
    > get the type of m, if int (this will not work b/c people can put in fractions for x/y points)
    > divide by 2, if r=1 or r=0 (maybe?)
'''

# todo: graph? (can you generate a graph using a turtle?)
''' 
  Pretty sure there is a way to import a math graph module for this
'''

# todo: reduce fractions
'''
    a. calculate m_dividend // m_divisor (int not float)
        -10/5 = -2
        3/5 = 0
        10/7 = 1
        10/4 = 2
    b. calculate m_dividend % m_divisor 
        r=0
        r=3
        r=3
        r=2
    if r=0 that means there is no denominator 
       and the output (slope "m") can be "a"
       
    if r>0 then we need to make it an improper fraction again
        c. calculate the numerator
            b*a + b 
            3*0 + 3
            3*1 + 3 = 6 [THIS DOES NOT WORK]
            2*2 + 2 = 6 [THIS DOES NOT WORK]
        how do we get 10/4 to 5/2
         > look into prime numbers...?  
'''

# end program
