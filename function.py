def factorial(n):
    if n<2:
        return 1
    return n*factorial(n-1)
n=int(input("enter the number: "))
s=factorial(n)
print(s)