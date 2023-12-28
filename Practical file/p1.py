# generating list using range function
n=int(input("enter range limit from o --> "))
list_1=list(range(0,n,2))
print("Creation of List of all even numbers in range 0 to 50 (inclusive) --->")
print(list_1)
# We can also print the in more user friendly way by using for loop
for i in list_1:
    print(i,end='  ')