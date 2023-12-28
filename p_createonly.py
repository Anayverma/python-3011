# Ques 2) Write a program in python to create a matrix of size 3X3 with variable name A taking input frm use.
A=[]
for row in range(0,3):
    row=[]
    for ele in range(0,3):
        row.append(int(input("enter an element => ")))
    A.append(row)
for r in A:
    for ele in r:
        print(ele,end="\t")
    print()
