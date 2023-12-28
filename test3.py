# def print_all_substrings(input_str):
#     n = len(input_str)
#     l=[]
#     for i in range(n):
#         for j in range(i + 1, n + 1):
#             substring = input_str[i:j]
#             if substring!=substring[::-1]:
#                 continue
#             l.append(substring)
#     l=sorted(l)
#     print(l)
# input_string = "level"
# print_all_substrings(input_string)
# def fibonacci(n):
#     if n<=1:  print(n)
#     else:
#         a,b,c=0,1,1
#         for i in range (n-2):
#             a,b=b,c
#             c=a+b
#         print(c)
# fibonacci(1)
def squareroot(xx):
    x=1
    for i in range(60):
        x=(x*x+xx)/(2*x)
    print(x)
squareroot(12688889899878786868657474838399999)
print(12688889899878786868657474838399999**0.5)
