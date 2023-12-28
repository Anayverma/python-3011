# Ques 10) WAP to demonstrate the use of control statements.
def if_else_if():
    num=int(input("Enter a Number => "))
    if num>0:
        print("Positive Number")
    elif num<0:
        print("Negative Number")
    else:
        print("Number is equal to zero")
        
if_else_if()