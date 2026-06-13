tup=(1,2,3,4,5,"krishna",3.14)
# tup[2]=10 error dega
print(tup[2])
tup1=(1) # bina , diye rakhenge to touple jaisa nii dega integer jaisa behave karega
print(type(tup1))
tup2=(1,)
print(type(tup2))

# slicing in tuples
print(tup[:3])

tup3=(1,2,3)

# loops in tupls

for val in tup:
    print(val)

# methods in tuple
tups=(1,2,2,3,2,4)
print(tups.index(2)) # first occurence of 2 index will=1

print(tups.count(2)) # total 2,2,2=3 times


