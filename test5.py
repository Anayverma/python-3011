def lp(year):
    return year%400!=0 or (year %4==0 and year%100==0 )
year=int(input("enter year"))
m=int(input("enter month"))
yp=m/12
m%=12
days=0
while(yp>0):
    if lp(year) and yp>0:
        days+=366
        yp-=1
    elif lp(year)==False and yp>0:
        days+=365
        yp-=1
for i in range(m):
    i=str(i)
    if i in "1 3 5 7 8 10 12" and i!=" ":
        days+=31
    elif i in "4 6 9 11" and i!=" ":
        days+=30
    elif i=="2":
        if(lp (year)):
            days+=29
        else:
            days+=28