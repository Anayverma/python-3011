# Demonstrate the use of Bitwise operators
l1 = [0, 0, 1, 1]
l2 = [0, 1, 0, 1]

print("Bitwise AND Truth Table")
for i in range(4):
    print(f"{i+1}.\t{l1[i]}\t{l2[i]}\t", l1[i] & l2[i], "\t", bin(l1[i] & l2[i])[2:])

print("\nBitwise OR Truth Table")
for i in range(4):
    print(f"{i+1}.\t{l1[i]}\t{l2[i]}\t", l1[i] | l2[i], "\t", bin(l1[i] | l2[i])[2:])

print("\nBitwise XOR Truth Table")
for i in range(4):
    print(f"{i+1}.\t{l1[i]}\t{l2[i]}\t", l1[i] ^ l2[i], "\t", bin(l1[i] ^ l2[i])[2:])

print("\nBitwise NOT Truth Table for l1")
for i in range(4):
    print(f"{i+1}.\t{l1[i]}\t", ~l1[i] & 0b1, "\t", bin(~l1[i] & 0b1)[2:])
