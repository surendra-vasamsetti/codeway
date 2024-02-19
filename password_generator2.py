import random
import string
print("Welcome to the RANDOM PASSWORD GENERATOR")
def main():

    length=int(input("Enter the length of the password"+":"))
    lowerL=string.ascii_lowercase
    upperL=string.ascii_uppercase
    digit=string.digits
    symbols=string.punctuation
    combine=lowerL+upperL+digit+symbols
    x=random.sample(combine,length)
    password="".join(x)
    print(password)
    main()
main()    
 