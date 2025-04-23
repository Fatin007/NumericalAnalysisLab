import math
#here f1 is the derivative of f. p0 is the initial guess. p is the next guess

def Newton(f,f1,p0,TOL,N0): 
    i=0
    print("  i       p0             p             |p-p0|")
    print("--------------------------------------------------")
    while i<=N0:
        p = p0-f(p0)/f1(p0)
        print(format(i,'3d'),'  ',format(p0,'10.8f'),'  ',format(p,'10.8f'),'  ',format(abs(p-p0),'10.8e'))
        if abs(p-p0)< TOL:
            return print('The solution is ', format(p,'10.8f'))
        i=i+1
        p0=p
    print('The method fails after N0 iterations')
    return None

f = lambda x: math.cos(x) - x
f1 = lambda x: - math.sin(x) - 1
Newton(f, f1, math.pi/4, 0.0000000000000001, 20)
print("--------------------------------------------------")