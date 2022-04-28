def prime(i):
    l=[9,8,7,6,5,4,3,2]
    for i in l[::-1]:
        b= 0
        for j in l:
            if i == j:
                pass
            if i%j != 0:
                b += 1
        if b== 7:
            print(i)
            
def pr(x):
    v= [9,8,7,6,5,4,3,2]
    c= 0
    for g in v:
        if x%g !=0:
            c += 1
        elif x%g ==0:
            pass
    if c== 8:
        print(x)



prime(i=0)
for x in range(10,101):
    pr(x)
    