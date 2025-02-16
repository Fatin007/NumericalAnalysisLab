def prod_cal(p,n):
    product = p
    for i in range(1,n):
        product = product*(p-i)
    return product

def fact(n):
    prod = 1
    for i in range(2,n+1):
        prod = prod*i
    return prod


# Number of data set n
n = 4
x = [1, 3, 5, 7]
# y[][] is used for difference table
# y[][0] is used for input
y = [[0 for i in range(n)] for j in range(n)]
y[0][0]= 24
y[1][0]= 120
y[2][0]= 336
y[3][0]= 720
# Calculating differne table
for i in range(1,n):
    for j in range(n-i):
        y[j][i]=y[j+1][i-1]-y[j][i-1]
# Display the difference table
for i in range(n):
    print(x[i], end="\t")
    for j in range(n-i):
        print(y[i][j], end="\t")
    print(' ')
# input the value of interpolation
value = 8
p = (value - x[0])/(x[1]-x[0])
sum = y[0][0]
for i in range(1,n):
    sum = sum + prod_cal(p,i)*y[0][i]/fact(i)
print('\n Value at', value, 'is', round(sum, 6))
