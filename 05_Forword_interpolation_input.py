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


# Taking user input for number of data points
n = int(input("Enter number of data points: "))
x = []
y = [[0 for i in range(n)] for j in range(n)]

# Taking user input for x values
print("Enter the x values:")
for i in range(n):
    x.append(float(input(f"x[{i}]: ")))

# Taking user input for y values
print("Enter the y values:")
for i in range(n):
    y[i][0] = float(input(f"y[{i}]: "))

value = float(input("\nEnter the value for interpolation: "))
# Calculating difference table
for i in range(1,n):
    for j in range(n-i):
        y[j][i]=y[j+1][i-1]-y[j][i-1]

# Display the difference table
print("\nForward Difference Table:")
for i in range(n):
    print(int(x[i]) if x[i].is_integer() else x[i], end="\t")
    for j in range(n-i):
        print(int(y[i][j]) if y[i][j].is_integer() else y[i][j], end="\t")
    print(' ')

# input the value for interpolation
p = (value - x[0])/(x[1]-x[0])
sum = y[0][0]
for i in range(1,n):
    sum = sum + prod_cal(p,i)*y[0][i]/fact(i)
print('\nValue at', value, 'is', round(sum, 6))
