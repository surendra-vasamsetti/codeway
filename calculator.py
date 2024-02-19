print("select an operation to performm: ")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVISON")
print("5.EXIT")

operation=int(input())


if operation==1:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number: "))
    sum=num1+num2
    print(f"The sum of {num1} and {num2} is {sum}.")
elif operation==2:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number: "))
    sub=num1-num2
    print(f"The subtraction of {num1} from {num2}  is {sub}.")
  
elif operation==3:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number: "))
    mul=num1*num2
    print(f"The multiplication of {num1} and {num2} is {mul}.")
    
elif operation==4:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number: "))
    div=num1/num2
    print(f"The divison of {num1} and {num2} is {div}")

elif operation==5:
    print("You are successfully exited:)")
    exit()
    
else:
    print("Invalid Entry.Please choose from the above options:)")