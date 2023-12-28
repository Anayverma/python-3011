# def no(n):
#     if n%2==0: print(n,"is even")
#     else: print(n,"is odd")

# def paplindrome(n):
#     m=n
#     num=0
#     while n!=0:
#         print(num)
#         r=n%10  
#         num=(num*10)+r
#         n=n//10
#     print(m==num)
# paplindrome(101)

# def anagrams(lis):
#     for i in range(len(lis)-1):
#         if sorted(list(lis[i]))!=sorted(list(lis[i+1])):
#             print("not")
#             return
#     print("true")
# anagrams(['listen', 'silent', 'enlista'])

# def pattern(n=5):
#     x=97
#     for i in range(n-1,-1,-1):
#         s=""
#         for k in range(i):
#             s+=" "
#         for j in range(i,n):
#             s+=chr(x)+" "
#             x+=1
#         print(s)
# pattern()

def check():
    l=[1,2,2,2,2,2,2,2,3]
    l.remove(2)
    l.remove(2)
    print(l)
check()