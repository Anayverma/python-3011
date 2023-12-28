def mutualfunds(amt,r):
    amt+=(r*amt)/100
    return amt
def lifeinsurance(amt,r):
    amt+=(r*amt)/100
    return amt
def asserts(amt,r):
    amt+=(r*amt)/100
    return amt
def fixeddeposits(amt,r):
    amt+=(r*amt)/100
    return amt
def increment(amt,r):
    amt=(r*amt)/100
    return amt
def main():
    mon_sal=int(input("Please enter MONTHLY salary ==>  "))
    tenure=int(input("Please enter YEARS of service ( tenure ) ==>  "))
    incr=int(input("Please enter ANNUAL INCREAMENT  PERCENT in  salary ==>  "))
    # sr=int(input("Please enter rate of percent for share market ==>  "))
    # mr=int(input("Please enter rate of percent for mutual funds ==>  "))
    # lr=int(input("Please enter rate of percent for life insurance ==>  "))
    # fr=int(input("Please enter rate of percent for fds ==>  "))
    # ar=int(input("Please enter rate of percent for assest  ==>  "))


    year_sal=mon_sal*12
    mf=0
    li=0
    fd=0
    ass=0
    sm=0
    temp=0
    total=year_sal
    for i in range (tenure-1):
        # temp=mutualfunds(.1*total,mr)
        mf=(.05*year_sal+mf) *1.05
        # temp=lifeinsurance(.05*year_sal,lr)
        li=(.03*year_sal+li) *1.05
        # temp=fixeddeposits(0.03 *year_sal,fr)
        fd=(.03*year_sal+fd) *1.05
        # temp=asserts(0.03*year_sal,ar)
        ass=(.04*year_sal+ass) *1.05
        sm=(.10*year_sal+sm) *1.10

        print(sm)
        # temp=increment(year_sal,incr)
        year_sal=year_sal*1.07
        total+=year_sal
    print()
    dif=.1*total
    print("total Share Market income ==",sm-dif)
    print("total income without investemnts ==",total)
    total=total-(dif*5)

    total+=mf+li+fd+ass+sm
    print("total income with investemnts ==",total)
main()



