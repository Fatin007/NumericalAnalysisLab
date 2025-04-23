n = int(input("Enter number of data points: "))
x = []
y = [[0 for _ in range(n)] for _ in range(n)]

print("Enter the x values:")
for i in range(n):
    x.append(float(input(f"x[{i}]: ")))

print("Enter the y values:")
for i in range(n):
    y[i][0] = float(input(f"y[{i}]: "))
    
value = float(input("\nEnter the value for interpolation: "))

# Calculating differne table
for i in range(1,n):
    for j in range(n-i):
        y[j][i]=(y[j+1][i-1]-y[j][i-1])/(x[j+i]-x[j])
# Display the difference table
for i in range(n):
    print(round(x[i],7), end="\t")
    for j in range(n-i):
        print(round(y[i][j],7), end="\t")
    print(' ')
# input the value of interpolation
sum = y[0][0]
product = 1
for i in range(1,n):
    product = product*(value-x[i-1])
    sum = sum + product*y[0][i]
print('\n Value at', value, 'is', round(sum, 7))
