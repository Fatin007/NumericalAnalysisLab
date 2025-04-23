def prod_cal(p, n):
    product = p
    for i in range(1,n):
        product = product*(p+i)
    return product

def fact(n):
    prod = 1
    for i in range(2, n + 1):
        prod *= i
    return prod

n = int(input("Enter number of data points: "))
x = []
y = [[0 for i in range(n)] for j in range(n)]

print("Enter the x values:")
for i in range(n):
    x.append(float(input(f"x[{i}]: ")))

print("Enter the y values:")
for i in range(n):
    y[i][0] = float(input(f"y[{i}]: "))

value = float(input("\nEnter the value for interpolation: "))

# Calculating difference table
for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

# Display the difference table
print("\nBackword Difference Table:")
for i in range(n):
    print(x[i], end="\t")
    for j in range(n - i):
        print(y[i][j], end="\t")
    print("")

# initializing u and sum
sum = y[n-1][0]
p = (value - x[n-1]) / (x[1] - x[0])
for i in range(1, n):
    sum = sum + (prod_cal(p, i) * y[n-i-1][i]) / fact(i)

print("\nValue at", value, "is", round(sum, 6))





