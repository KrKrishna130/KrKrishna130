# while loop
i=10
# infinite loop
# while True:
#     print("krishna")
count=1

while count <= 5:
    print("krishna")
    count+=1
# print 1-5 number

i=1
while (i<=5):
    print(i)  
    i +=1
# Reverse Loop
i=10
while(i>=1):
    print(i)
    i=i-1

# print No. of multiplication of 6
# i=1
# while(i<=10):
#     print(6*i)
#     i+=1

#==========Break and Continue============###
# when multple of 6 came then cames out from loop
# i=1
# while(i<=10):
#     if(i % 6==0):
#       break
#     print(i)
#     i+=1
# print("out side of loop")
print("==========continue=========")
i=1
while(i<=10):
    if(i % 3 ==0):
      i+=1
      continue
    print(i)
    i+=1
print("out side of loop")

# ============for loop================#
print("===============For Loop===================")
# string="hello"
# for var in string:
#     print(var)

string="hello"
# in operator works-to check presence value
if 'o' in string:
    print("o existing in string")
# range(n) -->give elements from 0 to n-1.
for i in range(5):
    print(i)

print("==========count i in artificial intelligence ====")
word="artificial intelligence"
count=0
for ch in word:
    if(ch=='i'):
        count+=1
print("count of i : ",count)


print("==========count vowels  artificial====")
word="artificial" #a,i,i,i,a=5
count=0
for ch in word:
    if(ch=='a' or ch=='e'  or ch=='i' or ch=='o' or ch=='u'):
        count+=1
print("count of i : ",count)

# range(start, stop,step)
# start -0 start krta hai,stop rokta hai,step +1 krk value deta hai
print("range(1,5)==>")
for el in range(1,5):
    print(el)

print("range(1,5,2)==>")
for el in range(1,5,2):
    print(el)

print("sum of first 6 numbers=======>")
sum=0
for i in range(1,6):
    sum +=i
print("sum==>",sum)

print("sum of first n numbers=======>")

n=int(input("enter number :"))

sum=0
for i in range(1,n+1):
    sum +=i
print("sum==>",sum)