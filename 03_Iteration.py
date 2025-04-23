def Iteration(g, p0, Tol, N0):
    i=1
    while(i<=N0):
        p=g(p0)
        print(format(i, '>4d'),' ', format(p0, '>12.8f'), ' ', format(p, '>12.8f'))
        if abs(p-p0) < Tol:
            return print("Solution is: ", format(p, '>12.8f'))
        i+=1
        p0=p
    print("Method failed after N0 iterations ")
    return None

# g2=lambda x: (10/(4+x))**0.5
# g3=lambda x: (10/(x**2 + 4))**0.5
# g4=lambda x: (10/(x**2 + 4))**0.5

# Iteration(g2, 1.5, .00001, 25)
# Iteration(g3, 1.5, .00001, 25)
# Iteration(g4, 1.5, .00001, 25)

inF = input("Enter the function: ")
g=lambda x: eval(inF)
p0=float(input("Initial guess: "))
TOL=float(input("Tolerance: "))
N0=int(input("Maximum num of iterations: "))

Iteration(g, p0, TOL, N0)