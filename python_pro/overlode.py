class model:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        return self .a +other.a
    def __add__(self,other):
        return self .a -other.a
    def __add__(self,other):
        return self .a *other.a
    def __add__(self,other):
        return self .a /other.a
x=model(10)
y=model(20)    
print(x/y)
    

        