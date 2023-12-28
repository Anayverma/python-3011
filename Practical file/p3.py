# Get the size of matrices as input
n = int(input("Enter the size of matrices (n x n): "))

# Input matrix A
A = []
print("Enter elements for matrix A:")
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input(f"Enter element at position ({i}, {j}): ")))
    A.append(row)

# Input matrix B
B = []
print("Enter elements for matrix B:")
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input(f"Enter element at position ({i}, {j}): ")))
    B.append(row)

# Initialize result matrix C with zeros
C = [[0 for _ in range(n)] for _ in range(n)]

# Matrix multiplication
for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]

# Display the result matrix C
print("Resultant Matrix C:")
for row in C:
    for ele in row:
        print(ele, end="\t")
    print()
