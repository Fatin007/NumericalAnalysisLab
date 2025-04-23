def bisection(f, a, b, TOL, N0):
    if f(a) * f(b) > 0:
        print("Bisection method fails.")
        return None
    i=1
    FA=f(a)
    print("   i          a              p              b            f(p)")
    while(i<=N0):
        p=(a+b)/2
        FP=f(p)
        print(format(i, '>4d'),' ', format(a, '>12.8f'), ' ', format(p, '>12.8f'), ' ', format(b, '>12.8f'), ' ', format(FP, '>12.8f'))
        if FP == 0 or abs(f(p)) < TOL:
            FP=f(p)
            return print("Solution is: ", p)
        i+=1
        if FA*FP > 0:
            a=p
            FA=FP
        else:
            b=p
    print("Method failed after N0 iterations ")
    return None

# f=lambda x: x**3 + 4*x**2 - 10
# f=lambda x: x**3 - x - 1
# f=lambda x: x**2 - 3

inF = input("Enter the function (e.g., x**3 + 4*x**2 - 10): ")
f=lambda x: eval(inF)
a=float(input("Enter the lower bound: "))
b=float(input("Enter the upper bound: "))
TOL=float(input("Enter the tolerance: "))
N0=int(input("Enter the number of iterations: "))

# bisection(f, 1, 2, 0.01, 25) 
bisection(f, a, b, TOL, N0)