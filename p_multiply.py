# Ques 4) find multiplication of 2 matrices A and B of size 3X3
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
C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            C[i][j]+=A[i][k]*B[k][j]

for r in C:
    for ele in r:
        print(ele,end="\t")
    print()
