
class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        print(self.id)
std=Student("Simon",1)
std.id=2
print(std.id)

class A():
    def __init__(self,count=100):
        self.count=count

obj1=A()
obj2=A(102)



print(obj1.count)



print(obj2.count)