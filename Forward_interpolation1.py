# This is a forward-difference interpolation formula
# calculate the product p(p-1)(p-2)...
def prod_cal(p, n):
    # n is the number of given data set
    product = p
    for i in range(1,n):
        product = product*(p-i)
    return product

# calculating factorial of given number n
def fact(n):
    prod = 1;
    for i in range(2, n + 1):
        prod *= i
    return prod

# Main code
# Number of values given
n = 4
x = [1, 3, 5, 7]
# y[][] is used for difference table
# with y[][0] used for input
y = [[0 for i in range(n)] for j in range(n)]
y[0][0] = 24;
y[1][0] = 120;
y[2][0] = 336;
y[3][0] = 720;
# Calculating the forward difference
# table
for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1];
  # Displaying the forward difference table
for i in range(n):
    print(x[i], end="\t");
    for j in range(n - i):
        print(y[i][j], end="\t");
    print(" ");

# Value to interpolate at
value = 8;

# initializing u and sum
sum = y[0][0];
p = (value - x[0]) / (x[1] - x[0]);
for i in range(1, n):
    sum = sum + (prod_cal(p, i) * y[0][i]) / fact(i);

print("\nValue at", value,
      "is", round(sum, 6));





