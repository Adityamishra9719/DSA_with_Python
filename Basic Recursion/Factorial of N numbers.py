def Factorial(n):
    if n < 1:
        return 1
    return n* Factorial(n - 1)

n = int(input("Enter the number : "))
print(Factorial(n))