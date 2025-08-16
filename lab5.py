#Book_class
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")

    def update_price(self, new_price):
        self.price = new_price

b = Book("Python Programming", "John Doe", 500)
b.display_info()
b.update_price(600)
b.display_info()

#student_class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_details(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = Student("Alice", 85)
s2 = Student("Bob", 90)
s3 = Student("Charlie", 78)
s1.show_details()
s2.show_details()
s3.show_details()

#bank_account_class
class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(f"Balance: {self.balance}")

acc = BankAccount("Alice", "12345", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.show_balance()

