def trapezoidal(f, a, b, n):
    h = float(b-a)/n;
    y = [0 for i in range(n+1)];
    y[0]=f(a);
    y[n] = f(b);
    result= h*(y[0]+y[n])/2;
    for i in range(1, n):
        y[i] = f(a + i*h)
        result +=  h*y[i]
    return result

from math import exp
v = lambda t: 3*(t**2)*exp(t**3)
n = 4
numerical = trapezoidal(v, 0, 1, n)
print(numerical)

