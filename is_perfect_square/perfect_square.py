import cmath
from decimal import *
def check_complex(val):
    comp = cmath.sqrt(val)
    return comp.real.is_integer() and comp.imag.is_integer()
def is_perfect_square(val,*,complex=False):
    if complex:
       return check_complex(val) 
    if val<0:
        return False
    b = Decimal(val).sqrt()
    return Decimal(int(b)**2)==Decimal(val)
