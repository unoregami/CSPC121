class Manager:
    def __init__(self, name, department, post="Manager"):
        self.__name = name
        self.__department = department.lower()
        self.__post = post
        self.__basic = None
        self.__houserent = None
        self.__transport = None
        self.__salary = None

    def post_detail(self):
        if self.__department == "hr":
            self.__basic = 30000
        else:
            self.__basic = 25000
        self.__houserent = 10000
        self.__transport = 5000
        print(f"The post of {self.__name} is {self.__post}")

    def salary(self):
        self.__salary = self.__basic + self.__houserent + self.__transport
        return self.__salary


class Clerk:
    def __init__(self, name, post="Clerk"):
        self.__name = name
        self.__post = post
        self.__basic = None
        self.__transport = None
        self.__salary = None

    def post_detail(self):
        self.__basic = 10000
        self.__transport = 2000
        print(f"The post of {self.__name} is {self.__post}")

    def salary(self):
        self.__salary = self.__basic + self.__transport
        return self.__salary


mr = Manager("Juan", "hr")
mr1 = Manager("Maria", "Accounting")
ck = Clerk("Pedro")
emp = [mr, mr1, ck]

for x in emp:
    x.post_detail()
    print(f"The salary is {x.salary()}\n")
