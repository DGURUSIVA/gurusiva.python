a=[1,8,5,8,887]
if len(a)%2==0:
    out=0
    for i in a:
        out +=i
else:
    out=1
    for i in a:
        out*=i
    print(out)
