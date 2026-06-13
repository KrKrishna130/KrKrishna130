info={
    "name":"krishna",
    "cgpa":9.3,
    "subject":["Math","Science"],
    3.14:"PI"

}
print(info)
print(type(info))
print(info["name"]) #print value of which have key as name

info["cgpa"]=7.9
print(info["cgpa"])
print(info)

# methods in dictionary
# find out keys
print("keys are :",info.keys())

# find out values
print("values are :",info.values())

# find out items
print("items are :",info.items())

# find out get values
print("get are :",info.get("name")) # name key exist hai
print("get are :",info.get("name34")) # name34 key hai hi nii but error ni aaya program me

# print(info["cgpa2"]) # ye eror deta hai,ye error dega program me

info.update({
        "city":"Mumbai"
    })

print(info)