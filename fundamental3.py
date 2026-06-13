String="hello"
print(String)
# concatenation
str="krishna"+"kumar"
print(str)

strs="Apna_College"
# str1[0]-->A
print(strs[0])

# immutable
#strs[0]='B' # this is not allowed becz string is immutable in python

# slicing
# strs[0,4]
print(strs[1:4]) #pna
print(strs[:4]) #bydefault 0 leta hai start me # Apna
print(strs[1:]) #bydefault lenght leta hai last me m #pna_College

print(strs[:]) # bydefault 0 -last index leta hai


# Reverse indexing
str2="Apple"
print(str2[-3:-1]) #pl
print(str2[-5:-2])

# String formatting
a=10
b=5
sum=a+b
print("sum is->",sum)
print("sum is {}".format(sum))
print("sum is {} {} {}".format(a,b,sum))
print("sum {} is {}".format(a,b,sum))
print("==================")
# indexes based fomating
print("sum of {1} & {0} is {2}".format(a,b,sum))

# value based fomating
print("value of {c} & {d}".format(c=7,d=7))

print("=== f string ============")

# F-String way of foramtting string
m=5
n=10
print(f"sum of {m} & {n} is {m+n}")
