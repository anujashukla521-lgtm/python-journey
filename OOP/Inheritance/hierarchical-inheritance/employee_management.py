class Employee:
    def work(self):
        print("Employee works")

class Manager(Employee):
    def work(self):
        print("Manager works")

class Developer(Employee):
    def work(self):
        print("Developer works")

class Designer(Employee):
    def work(self):
        print("Designer works")

manager = Manager()
dev = Developer()
design = Designer()

manager.work()
dev.work()
design.work()