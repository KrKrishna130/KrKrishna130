s={1,2,3,4,2,3}
print(s)

print(type(s))
print(len(s))

s.add(7)
print(s)

empty_set={}
print(type(empty_set))

null_set=set()  #empty set syntax
print(type(null_set))

s.remove(2)
print(s)
s.clear()
print(s)

# union of set
s1={1,2,3,4,5}
s2={4,5,8,9,10}

print(s1.union(s2))
# for find out common(intersection)
print(s1.intersection(s2))


# Practice
info=[
    {"bob","Math"},
    {"Alice","Math"},
    {"rony","physics"},
    {"jony","Math"},
    {"joy","science"},
    {"yogi","histoy"},
]

course_set=set() # empty set
for tup in info:
    course_set.add(tup[1])

    print(course_set)