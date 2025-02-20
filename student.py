from thursday import User
class Student(User):
    def __init__(self,name,password):
        super().__init__(name,password)
        pass
    def login(self):
        input("Firrst enter your password:")
        super().login()
    pass


student1 = Student("Rohan","1234")
print(student1.name)
print(student1.pswd)
student1.login()

class MyString(str):
    pass

# print(dir(MyString))

def add(x,y):
    return x+y

# (x,y)=>{x+y}
# lambda params: function_body
lambda x,y: x+y 