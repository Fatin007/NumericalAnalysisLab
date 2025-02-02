def Iteration(g, p0, Tol, N0):
    i=1
    while(i<=N0):
        p=g(p0)
        print(format(i, '>4d'),' ', format(p0, '>12.8f'), ' ', format(p, '>12.8f'))
        if abs(p-p0) < Tol:
            return print("Solution is: ", p)
        i+=1
        p0=p
    print("Method failed after N0 iterations ")
    return None

g1=lambda x: (10/x - 4*x)**0.5
g2=lambda x: (10/(4+x))**0.5
g3=lambda x: (10/(x**2 + 4))**0.5
g4=lambda x: (10/(x**2 + 4))**0.5

Iteration(g1, 1.5, .00001, 25)
print()
Iteration(g2, 1.5, .00001, 25)
print()
Iteration(g3, 1.5, .00001, 25)
print()
Iteration(g4, 1.5, .00001, 25)
print()