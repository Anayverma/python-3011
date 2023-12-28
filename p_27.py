# Demonstrate the use of Control statements.
def calc_sum(n):
    sum_result=0
    for i in range(1,n+1):
        sum_result+=i
    return sum_result
def main():
    n=int(input("Enter a Number => "))
    result=calc_sum(n)
    print(result)
__int__=main()