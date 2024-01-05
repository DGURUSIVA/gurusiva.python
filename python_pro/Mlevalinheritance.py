class Grand:
    def _init_(self,c,d):
        self.c=c
        self.d=d
class parent(Grand):
    def _init_(self,c,d,e,f):
       super()._init_(c,d,)
       self.e=e
       self.f=f
class child(parent):
    def _init_(self,c,d,e,f,g,h):
       super()._init_(c,d,e,f)
       self.g=g
       self.h=h
obj=child(20,30,40,50,60,70)
print(obj.g)

      

        