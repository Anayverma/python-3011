# Ques 3) Summation of two matrices of size 3X3.
A=[]
for row in range(0,3):
    row=[]
    for ele in range(0,3):
        row.append(int(input("enter an element => ")))
    A.append(row)
B=[]
for row in range(0,3):
    row=[]
    for ele in range(0,3):
        row.append(int(input("enter an element => ")))
    B.append(row)
C=[]
for i in range(0,3):
    row=[]
    for j in range(0,3):
        row.append(A[i][j]+B[i][j])
    C.append(row)

for r in C:
    for ele in r:
        print(ele,end="\t")
    print()
