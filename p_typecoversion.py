# Ques 9) WAP to demonstrate the use of type conversion.
def type_con():
    num_int=10  
    num_str=str(num_int)
    print("Integer to String")
    print(num_int,"Type = ",type(num_int))
    print(f"{num_int}+10  = ",num_int+10)
    print(num_str,"Type = ",type(num_str))
    print(f"{num_int}+10  = ",num_str+"10")

type_con()