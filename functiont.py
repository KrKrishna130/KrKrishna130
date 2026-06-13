# basic function
# yaha hm fun ko define kr rahe hai
def hello():
    print("hello")

# yaha us fun ko call kr rahe hai
hello()

# parameter(define time input) vs arguments(actual input value)
def sum(a,b): #here a,b -parameter
    s=a+b
    return s

print(sum(2,3)) #here 2,3 is arguments hai

#==========default value===============

def sum1(a,b=1):
    return a+b
print(sum1(5)) #5+1(default value)
print(sum1(5,7)) # 5+7

# ========lambda fun================#
suml=lambda a,b,c:a+b+c
# call
print(suml(4,5,8))

avg=lambda a,b,c:(a+b+c)/3
# call
print(avg(4,5,8))

# calculate factorial
def calc_factorial(n):
    fact=1
    for i in range(1,n+1):
        fact *=i
        
    return fact
n=int(input("enter n:"))

print(calc_factorial(n))



