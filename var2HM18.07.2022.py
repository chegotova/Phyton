# Вычислить число c заданной точностью d. Число Пи не просто обрезать с math.pi, а вычислить, используя формулы: Нилаканта, ряды Тейлора, серию Ньютона или серию Чудновских.


import math
from decimal import *
from time import time


def bellard(n):
    pi = Decimal(0)
    k = 0
    while k < n:
      pi += (Decimal(-1)**k/(1024**k))*( Decimal(256)/(10*k+1) + Decimal(1)/(10*k+9) - Decimal(64)/(10*k+3) - Decimal(32)/(4*k+1) - Decimal(4)/(10*k+5) - Decimal(4)/(10*k+7) - Decimal(1)/(4*k+3))
      k += 1
    pi = pi * 1/(2**6)
    return pi

print ("bellard")
start = time()
my_pi = bellard(1)
print ("Pi = {}".format(str(my_pi)))
print("Time", time()-start)
  
  