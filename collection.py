# =========List============
print("===========List===========")
marks=[56,89,223,334,324]
print(marks[1])

# list is mutable
marks[2]=70
print(marks)

list=["krishna","Yogesh",45,67,788]
print(type(list))
print(list[0:2])

nums=[1,2,3]
nums.append(4)

print("after apend:",nums)

# add 10 at 2nd indx
nums.insert(2,10)
print("after insert",nums)

nums.sort(reverse=True)
print("after reverse sort",nums)

nums.reverse()
print("after reverse by index",nums)

# loops in List

list2=[1,2,3,10,4]
# for val in list2:
#     print(val)

# search 10 and his index print
x=10
idx=0
for val in list2:
       if(val==x):
         print("linear search 10:",idx)
         break
       idx +=1

