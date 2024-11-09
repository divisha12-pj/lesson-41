#calculator
def add(a,b):
    return a+b
def product(a,b):
    return a*b
def difference(a,b):
    return a-b
def div(a,b):
    return a//b



n1=int(input("enter a number"))
n2=int(input("enter a number"))
print("the sum of",n1,"and",n2, "is",add(n1,n2))
print("the product of",n1,"and",n2, "is",product(n1,n2))
print("the difference of",n1,"and",n2, "is",difference(n1,n2))
print("the quotient of",n1,"and",n2, "is",div(n1,n2))
