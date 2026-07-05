# Deal with json
import json
json_str='{"name":"krishna","isTeacher":true}'
# json me null,true hota hai->python me True,None hota hai
print(json_str)
print(type(json_str))# data type string hai

# convert into python
py_obj=json.loads(json_str)
print(type(py_obj),py_obj) # python data formate me convert ho jaega=dict

# Convert into python obj to json
py_obj1={"name":"krishna",
        #  "isTeacher":True,True,None python me hai
        "isTeacher":None
         }
json_str1=json.dumps(py_obj1)
print(type(json_str1),json_str1)
