class User:

    # greeting = "Umesalimiwa na User"

    def __init__(self, name_received,password_received):
        print(self, "has been initialized")
        self.name = name_received #creating a new attribute and asigning a value
        self.pswd = password_received
        # instance.attribute = value
        pass

    @property
    def pswd(self):
        return self.__password
    
    @pswd.setter
    def pswd(self,new_password):
        if type(new_password) != str:
            # print("here")
            raise ValueError("Password can only be string")
        else:
            self.__password = new_password
        return "Password Changed"

    # def get_password(self):
    #     # read a protected/private attribute
    #     return self._password
    
    # def set_password(self,new_password):
    #     if type(new_password) != str:
    #         return("Password can only be string")
    #     else:
    #         self._password = new_password
    #     return "Password Changed"


    # password = property(get_password,set_password)


    def change_greeting(self, new_greeting):
        self.greeting = new_greeting
        pass

    # def __init__(self,name,password):
    #     self.name = name
    #     self.password = password        
    #     pass

    def login(self):
        print(self)
        print("User has logged in")
        pass
    @classmethod
    def count_users(cls):
        print(cls)
        print("Counting total users")
        pass
    pass

if __name__ == "__main__":

    user1 = User() #object or instance
    user2 = User("Jafaar",123)
#user1 => Instance
# User => class
# user1.login()
# user1.random_attr = "Random"
# User.count_users()
# print(user1.name)
# print(user2.name)

# user1.change_greeting("Niaje msupa")
# print(user1.greeting)
# print(user2.greeting)
# Class
# object
# instantiation/initialization
# methods => a function that exists inside a class.Class method and Instance method. Impact behavior
# attributes => a variable used to store data related to the class or instance.Class Attributes and Instance Attributes
# properties => an attribute, conrolled using a method.

# private, protected, public

