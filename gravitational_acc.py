import math
from decimal import *
setcontext(Context(prec=100))
getcontext().prec = 100
def big(y,z):
    return 9.806160*(1-0.0026373*math.cos(2*y)+5.9*(10**(-6))*(math.cos(2*y))**2)-(3.085462*(10**(-4))+2.27*(10**(-7))*math.cos(2*y))*z+(7.254*(10**(-11))+1*(10**(-18))*math.cos(2*y))*(z**2)-(1.517*(10**(-17))+6*(10**(-20))*math.cos(2*y))*(z**3)
print(round(big(90,10000),8))
