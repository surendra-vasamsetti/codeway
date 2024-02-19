print("(:-----------------WELCOME TO PYCALCULATOR-------------------------:)")
print(":PLEASE ENTER TWO NUMBERS BELOW:")
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
ch=0
while ch<5:
    print("CALCULATOR MENU")
    print("1.ADD")
    print("2.SUBTRACT")
    print("3.MULTIPLY")
    print("4.DIVISON")
    print("5.EXIT")
    ch=int(input("enter your choice:"))
    if ch==1:
        c=a+b
        print(f"The sum of two numbers are {c}")
    elif ch==2:
        c=a-b
        print(f"The subtraction of two numbers are {c}")
    elif ch==3:
        c=a*b
        print(f"The multiplication of two numbers are {c}")
    elif ch==4:
        c=a/b
        print(f"The divison of two numbers are {c}") 
    elif ch==5:
        print("You are successfully exited:)")
        break
    else:
        print("INVALID OPTON.")           
