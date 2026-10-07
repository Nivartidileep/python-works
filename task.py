'''#Task : Convert same to Hierarchical also make use of public private,
#along with classmethods,class variables usage.
class Employee:
    # Class variable
    company_name = "Tech Solutions"

    def __init__(self, name, employee_id, salary):
        # Public attribute
        self.name = name

        # Private attribute
        self.__employee_id = employee_id

        # Public attribute
        self.salary = salary

    # Public method
    def display_employee(self):
        print("Name:", self.name)
        print("Employee ID:", self.__employee_id)
        print("Salary:", self.salary)
        print("Company:", Employee.company_name)

    # Class method
    @classmethod
    def change_company(cls, new_company):
        cls.company_name = new_company


# Child class 1
class Developer(Employee):

    def __init__(self, name, employee_id, salary, language):
        super().__init__(name, employee_id, salary)
        self.language = language

    def display_developer(self):
        self.display_employee()
        print("Programming Language:", self.language)


# Child class 2
class Tester(Employee):

    def __init__(self, name, employee_id, salary, testing_tool):
        super().__init__(name, employee_id, salary)
        self.testing_tool = testing_tool

    def display_tester(self):
        self.display_employee()
        print("Testing Tool:", self.testing_tool)


# Objects
developer1 = Developer("Dileep", 101, 30000, "Python")

tester1 = Tester("Rahul", 102, 28000, "Selenium")


# Display details
print("----- Developer Details -----")
developer1.display_developer()

print("\n----- Tester Details -----")
tester1.display_tester()


# Changing class variable using classmethod
Employee.change_company("ABC Technologies")

print("\nAfter changing company:")

print("Developer Company:", developer1.company_name)
print("Tester Company:", tester1.company_name)
#2.2
class TechnicalSkills:

    def coding(self):
        print("Employee can write Python programs.")

    def database(self):
        print("Employee can work with MySQL.")


class CommunicationSkills:

    def speaking(self):
        print("Employee has good communication skills.")

    def teamwork(self):
        print("Employee can work effectively in a team.")


# Multiple Inheritance
class SoftwareDeveloper(TechnicalSkills, CommunicationSkills):

    def employee_details(self):
        print("Role: Python Full Stack Developer")


# Object
developer = SoftwareDeveloper()

developer.employee_details()

developer.coding()
developer.database()

developer.speaking()
developer.teamwork()


#2.1
class BankAccount:

    # Class variable
    bank_name = "ABC Bank"

    def __init__(self, customer_name, account_number, balance):
        # Public attribute
        self.customer_name = customer_name

        # Private attribute
        self.__account_number = account_number

        # Public attribute
        self.balance = balance

    # Public method
    def display_account(self):
        print("Customer Name:", self.customer_name)
        print("Account Number:", self.__account_number)
        print("Balance:", self.balance)
        print("Bank:", BankAccount.bank_name)

    # Class method
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name


# Child class 1
class SavingsAccount(BankAccount):

    def __init__(self, customer_name, account_number, balance, interest_rate):
        super().__init__(customer_name, account_number, balance)

        # Public attribute
        self.interest_rate = interest_rate

    def display_savings(self):
        self.display_account()
        print("Interest Rate:", self.interest_rate)


# Child class 2
class CurrentAccount(BankAccount):

    def __init__(self, customer_name, account_number, balance, overdraft_limit):
        super().__init__(customer_name, account_number, balance)

        # Public attribute
        self.overdraft_limit = overdraft_limit

    def display_current(self):
        self.display_account()
        print("Overdraft Limit:", self.overdraft_limit)


# Objects
savings = SavingsAccount(
    "Dileep",
    "SB101",
    50000,
    6.5
)

current = CurrentAccount(
    "Rahul",
    "CA102",
    75000,
    25000
)


print("----- SAVINGS ACCOUNT -----")
savings.display_savings()

print("\n----- CURRENT ACCOUNT -----")
current.display_current()


# Calling class method
BankAccount.change_bank_name("XYZ Bank")

print("\n----- AFTER CHANGING BANK NAME -----")

print("Savings Account Bank:", savings.bank_name)
print("Current Account Bank:", current.bank_name)

