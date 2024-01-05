a=str(input())
i=0
count=0
while i<len(a):
    if a[i]in 'a,e,i,o,u':
        count+=1
    i=i+1
print(count)