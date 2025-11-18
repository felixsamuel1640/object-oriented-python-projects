class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def details(self):
        print("Employee Details")
        print(f"Employee name: {self.name}")
        print(f"Employee salary: ${self.salary:,.0f}")


class Manager(Employee):

    def manage(self):
        print(f"{self.name} is managing the team")

    # Overriding the parent method
    def details(self):
        print(f"{self.name} earns ${self.salary:,.2f}")


manager = Manager("Bernard Hackwell", 20000)

manager.manage()
manager.details()

