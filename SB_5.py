class Email:

    def __init__(self, fname, lname, num):
        self.fname = fname[0]
        self.lname = lname
        self.num = num+1
    company = "dlsud.edu.ph"

    def __str__(self):
        return f"{self.num}. {self.fname}{self.lname}@{self.company}"


print("Welcome to Email Generator App!\n===============================")
i = 0
email = []
conf = input("Add Name?: ").lower()
while conf == "yes":
    fn = input("Enter your first name: ").lower()
    ln = input("Enter your last name: ").lower()
    obj = Email(fn, ln, i)
    email.append(obj.__str__())
    conf = input("Add Name?: ").lower()
    i += 1

print("===============Generated Email===============\n")
for x in email:
    print(x)
