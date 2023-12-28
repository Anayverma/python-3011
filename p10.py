#  python program in which an function (with single string parameter ) is defined 
# and calling that function prints the string parameters given to function.


def func_print(para): # parameter passed
    print("String parameter received --\n{}".format(para))

para=input("Enter a String  -->  ")
func_print(para)   # calling the function
