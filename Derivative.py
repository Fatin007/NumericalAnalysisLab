import math
f = lambda x: x*math.exp(x)
h = 0.2
x0 = 2.0
# Three-point endpoint formula
Df_x0 = (-3*round(f(x0),6)+4*round(f(x0+h),6)-round(f(x0+2*h),6))/(2*h)
print('The derivative of f at x0 (By three-point endpoint formula):\n', round(Df_x0,6))
# Three-point midpoint formula
Df_x0 = (round(f(x0+h),6)-round(f(x0-h),6))/(2*h)
print('The derivative of f at x0 (By three-point midpoint formula):\n',  format(Df_x0,'>12.2e'))
