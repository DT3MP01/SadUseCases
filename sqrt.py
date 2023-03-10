# Find square root of real or complex numbers
# Importing the complex math module
import cmath
import sys

myArgs = sys.argv[1:]
num = int(myArgs[0])

# To take input from the user
#num = eval(input('Enter a number: '))

num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))