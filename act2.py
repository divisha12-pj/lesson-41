#recursive function
def fact(num):
    if num==1:
       return num
    else :
        return num*fact(num-1)


n=int(input("enter number"))
if n <=0:
    print ("sorry cannot find a factorial")
else :
    print("factorial of",n,"is",fact(n))



