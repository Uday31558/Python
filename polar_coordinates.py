import math
import cmath 
z = complex(input())


r = z.real*z.real+z.imag*z.imag

ph = cmath.phase(complex(z.real,z.imag))

print(math.sqrt(r))
print(ph)

