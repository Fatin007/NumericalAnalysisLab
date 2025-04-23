def iteration(g,p0,Tol,N0):
    i=1
    while i<=N0:
        print(i, ' ', p0)
        p = g(p0)       # Compute p
        if abs(p-p0)<Tol:
            return print('The solution is:', p)
        i=i+1
        p0 = p          # Update p0
    print('The method faied after', N0, 'iterations.')

g4 = lambda x: (10/(4+x))**0.5
#g5 = lambda x: x-(x**3+4*x**2-10)/(3*x**2+8*x)
iteration(g4,1.5,0.000000000001,30)
#iteration(g5,1.5,0.00001,30)