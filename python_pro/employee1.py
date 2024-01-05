class Employee:
    company = 'Tesla'
    ceo     = 'Elon musk'
    def insert_member(obj,name,age,sal,eid):
        obj.name = name
        obj.age  = age
        obj.sal  = sal
        obj.eid  = eid 

siva=Employee()
gopi=Employee()
dhoni=Employee()
Employee.insert_member(siva,'siva',22,50000,33)
Employee.insert_member(gopi,'gopi',22,50000,39)
dhoni.insert_member('DHONI',45,100000,'TES03')
a=siva.eid
print(a)