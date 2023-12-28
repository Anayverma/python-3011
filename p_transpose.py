# Ques 5) find transpose of a 3X3 matrix
A=[]
for row in range(0,3):
    row=[]
    for ele in range(0,3):
        row.append(int(input("enter an element => ")))
    A.append(row)
print("Original Array -->")
for r in A:
    for ele in r:
        print(ele,end="\t")
    print()
for i in range(0,3):
    for j in range(i,3):
        t=A[i][j]
        A[i][j]=A[j][i]
        A[j][i]=t
print("Transposed Array -->")
for r in A:
    for ele in r:
        print(ele,end="\t")
    print()

