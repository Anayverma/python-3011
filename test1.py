import random
l = [
    "22BCE10098", "22BCE10281", "22BCE10576", "22BCE10927", "22BCE11082",
    "22BCE11239", "22BCE11543", "22BCE10015", "22BCE10027", "22BCE10057",
    "22BCE10061", "22BCE10120", "22BCE10150", "22BCE10153", "22BCE10227",
    "22BCE10249", "22BCE10250", "22BCE10304", "22BCE10340", "22BCE10377",
    "22BCE10401", "22BCE10528", "22BCE10544", "22BCE10593", "22BCE10686",
    "22BCE10719", "22BCE10728", "22BCE10768", "22BCE10789", "22BCE10831",
    "22BCE10851", "22BCE10867", "22BCE10907", "22BCE10910", "22BCE10925",
    "22BCE10938", "22BCE10939", "22BCE10940", "22BCE10963", "22BCE11008",
    "22BCE11015", "22BCE11035", "22BCE11054", "22BCE11062", "22BCE11207",
    "22BCE11211", "22BCE11228", "22BCE11234", "22BCE11245", "22BCE11256",
    "22BCE11328", "22BCE11345", "22BCE11363", "22BCE11398", "22BCE11429",
    "22BCE11461", "22BCE11469", "22BCE11492", "22BCE11493", "22BCE11520",
    "22BCE11523", "22BCE11534", "22BCE11545", "22BCE11568", "22BCE11601",
    "22BCE11602", "22BCE11605", "22BCE11612", "22BCE11627", "22BCE11634"
]

i=1
while len(l)!=0:
    lt=[]
    while len(lt)!=5:
        m=random.randint(0,len(l)-1)
        lt.append(l[m])
        l.remove(l[m])