# Demonstrate the use of Logical operators 
l1=[0,0,1,1]
l2=[0,1,0,1]
print("AND Truth Table")
for i in range(0,4):
    print(f"{i+1}.\t{l1[i]}\t{l2[i]}\t",l1[i] and l2[i],"\t",bool(l1[i] and l2[i]))
print()
print("OR Truth Table")
for i in range(0,4):
    print(f"{i+1}.\t{l1[i]}\t{l2[i]}\t",l1[i] or l2[i],"\t",bool(l1[i] or l2[i]))
print()
print("NOT Truth Table")
for i in range(0,4):
    print(f"{i+1}.\t{l1[i]}\t", int(not l1[i]) ,"\t",(not l1[i] ))
print()