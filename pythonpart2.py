age=3

# if age>=18:
#     print("You can vote")
# else:
#     print("U cant vote")

    # if elif else
color=input("enter color is :")

if color=="red":
       print("stop bhai")
elif color=="green":
     print("Go !! jao bhai")
elif color=="yelow":
       print("Wait!!!")
else:
   print("wrong color")

#    condition with Retaional operator

age =int(input("enter age:"))
if(age<13):
      print("Child")
elif(age>=13 and age<18):
      print("Teenager")
else:
      print("adult")

    #   user login logic
username=input("Enter username:")
password=input("enter your password:")

if(username=="admin" and password=="pass"):
  print("user login successfully!!!!")
elif(username!="admin" and password=="pass"):
     print("enter correct username")
elif(username=="admin" and password!="pass"):
     print("enter correct password") 
else:
 print("Kindly enter correct username or password")

#  logic any number even or odd
n=int(input("enter number"))
if(n % 2==0):
 print("even")
else:
 print("odd")

#  Traffic scenario
colors=input("enter color:")
match colors:
    case"Green":
        print("Go")
    case "Red":
        print("Stop")
    case "Yellow":
        print("wait")
    # default
    case _:
        print("wrong color selection")
     
