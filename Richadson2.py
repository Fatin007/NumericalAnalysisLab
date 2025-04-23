import math
def D(Func,a,h):    # centered finite difference with step size h at point x=a
	return (Func(a+h)-Func(a-h))/(2*h)

def Richardson_dif(func,a):
    '''Richardson extrapolation method for numerical calculation of first derivative '''
    j=8# you can change the order of approximation but try keeping it under 10 to circumvent round-off errors.
    N=[[0 for i in range(j)] for k in range(j)];
    for I in range(j):
        N[I][0]=D(func,a,1/(2**(I+1)))
    for k in range(1,j):
        for i in range(j-k):
            N[i][k]=((2**(k))*N[i+1][k-1]-N[i][k-1])/(2**(k)-1)
    return N[0][j-1]
print('Numerical differentiation of Func=ln x at x=1.8')
f = lambda x: math.log(x);
print('%04.20f'%Richardson_dif(f, 1.8))
#################
#print('diff(2**cos(pi+sin(x)) at x=pi/2 is equal to = %04.20f'%Richardson_dif(lambda x: 2**cos(pi+sin(x)),pi/3))
# next up, how to implement higher order differentiation with a few tweaks in this code and how to do do partial derivation.