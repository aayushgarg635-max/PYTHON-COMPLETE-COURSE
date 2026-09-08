a =  int(input("Enter your age: "))

# IF ELIF ELSE LADDER
# START OF FIRST IF STATEMENT

if(a%2 == 0):
        print(" a is even")

# END OF FIRST IF STATEMENT
# START OF 2ND IF STAEMENT
if(a>18):
    print("you are above the age of consent")
    print("this is good for you")
elif(a<0):
    print("you are entering an invalid age")

elif(a==0):
    print("you are entering an not valid age")
     
else:
    print("you are below the age of consent")

# END OF 2ND IF STATEMENT

print("End of programme")