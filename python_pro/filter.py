def name (a):
    if a%2==0:
        return True
    else:
        return False
out = filter(name,[2,5,6,89,10,5])
print(list(out))    