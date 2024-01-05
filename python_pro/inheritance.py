class Base:
    a=10
    b=20
    def _init_(self,c):
        self.c = c
class derived(Base):
    def _init_(self,c,d,e):
        Base._init_(self,c)
        self.e = e
        self.d = d


obj = derived(6,58,56)        
    