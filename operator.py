a=30
b=10
# Arithmatic operators
# + operator
sum=a+b
print(sum)
print("Sum",a+b)
print("Sub",a-b)
print("mul",a*b)
print("div",a/b)
print("mod",a%b)
p=10
q=6
print("10 to power 6=",p**q)

# Relational Operator
R=2
S=3
print("== Operator->",R==S)
print("> operator->",R>S)
print("!= operaotr->",R!=S)
# Assignment Operator
M=23
N=78
# M=M+5 or M+=5
M+=5
print(M)
M -=5  # means M=M-5
print(M)

# Logical operator
print("OR=",3>2 or 4<3)
print("OR=",3>2 or 4<5)
print("OR=",3>6 or 4<6)

print("AND=>",4>3 and 6>5)
print("AND=>",4>5 and 6>5)
print("AND=>",4>3 and 6>8)

# Type conversion
E=10 #int
F=5 #int
print("E/F=",E/F) #decimal 2.0 apne aap type convert ho raha hai
ans=54+10.5
print("ans",ans)

#TypeCasting
L,M=1,"2"
O=int(M)
sum=L+O
print("after Typecaste=>",sum)
print(type(sum))

ans1=int(3+5.0)
# print("ans1",ans1)


ans2=5+10.5
# print("ans2",ans2)
print(ans1,type(ans1))
print(ans2,type(ans2))

val1=int("123")
print(val1,type(val1))


# Input from user
a=input("enter value of a:=")
print(a)

username=input("enter value of username:=")
print("Username",username)
a=input()
# by default input string leta hai
r=input("r value= ")
s=input("s value=")
sum=r+s
print(sum)

# Type conversion in input
c=int (input("c value= "))
d=int (input("d value="))
sum1=c+d
print(sum1)

input1=int(input("value1 is:"))
input2=int(input("value2 is:"))
avg=(input1+input2)/2
print(avg)