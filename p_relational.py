# Demonstrate the use of Relational operators
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(">")
if(a>b):
    print(f"{a} is GREATER than {b}")
else:
    print(f"{a} is NOT GREATER than {b}")

print("<")
if(a<b):
    print(f"{a} is LESSER than {b}")
else:
    print(f"{a} is NOT LESSER than {b}")
print(">=")
if a >= b:
    print(f"{a} is GREATER THAN OR EQUAL TO {b}")
else:
    print(f"{a} is NOT GREATER THAN OR EQUAL TO {b}")
print("<=")
if a <= b:
    print(f"{a} is LESSER THAN OR EQUAL TO {b}")
else:
    print(f"{a} is NOT LESSER THAN OR EQUAL TO {b}")
print("==")
if a == b:
    print(f"{a} is EQUAL TO {b}")
else:
    print(f"{a} is NOT EQUAL TO {b}")
print("!=")
if a != b:
    print(f"{a} is NOT EQUAL TO {b}")
else:
    print(f"{a} is EQUAL TO {b}")
