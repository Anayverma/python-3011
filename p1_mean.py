l=[]
n=int(input("Enter Size of Data Set => "))
for i in range(1,n+1):
    l.append(int(input(f"Please enter element {i} => ")))
print("Data Set Given : ",l)
# Calculating MODE
sum=0
f={}
for i in l:
    sum+=i
    if i not in f:
        f[i]=1
    else :
        f[i]=f[i]+1
mean=sum/n
print("MEAN = ",mean)
mode=[]
mx=max(f.values())
for i in f.keys():
    if f[i]==mx:
        mode.append(i)
print("MODE = ",mode)
if n%2==0:
    median=sorted(l)[n//2]
else:
    median = (sorted(l)[n//2] + sorted(l)[(n-1)//2]) / 2   
print("MEDIAN  = ",median)
var=0
for e in l:
    var+=(e-mean)**2
var=var/n
print("VARIANCE = ",var)
sd=var**0.5
print("STANDARD DEVIATION = ",sd)



