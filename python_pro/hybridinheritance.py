class add3:
    @staticmethod
    def add(a,b,c):
        return a+b+c
class add2:
    @staticmethod
    def add(a,b):
        return a+b
class add(add2,add3):
    pass    
class sub2:
    @staticmethod
    def add(a,b):
        return a-b
class cal(add,sub2):
    pass
obj = cal()
obj.add(4,5)
obj.sub(2,3)
