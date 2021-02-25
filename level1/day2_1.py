#간단한 수식
print ( 2 + 3 * 4)      # 14
print ( (2+3)*4)        # 20 

number = 2+3*4          # 14
print ( number )

number = number + 2     # 16
print(number)           # 16

number += 2
print (number)          # 18

number *= 2             # 36
print (number)

number /= 2             # 18
print (number)

number -= 2              # 16
print (number)

number %=  2            
print (number)          # 0

# 숫자 처리 함수

print (abs(-5))         # 5
print (pow(4,2))        # 4^2 = 4*4 = 16
print (max(5,12))       # 12
print (min(5,12))       # 5

print (round(3.14))     # 반올림 3 
print (round(3.54))     # 4

from math import *

print (floor(3.54))     # 내림 3
print (ceil ( 2.11))    # 올림 3
print (sqrt( 9))        # 제곱근 3