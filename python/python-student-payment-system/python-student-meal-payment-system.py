# Student class
class Student:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.breakfast = 0
        self.lunch = 0
        self.dinner = 0

    def show_balance(self):
        print("Current balance:", self.balance)

    def pay_meal(self, meal_type):
        print("Balance before purchase:", self.balance)

        if meal_type == "breakfast":
            price = 200
            meal_name = "Breakfast"
        elif meal_type == "lunch":
            price = 500
            meal_name = "Lunch"
        elif meal_type == "dinner":
            price = 250
            meal_name = "Dinner"
        else:
            print("Invalid meal type")
            return

        if self.balance >= price:
            self.balance -= price

            if meal_type == "breakfast":
                self.breakfast += 1
            elif meal_type == "lunch":
                self.lunch += 1
            elif meal_type == "dinner":
                self.dinner += 1

            print(meal_name, "price:", price)
            print("Amount deducted:", price)
            print("Balance after purchase:", self.balance)
        else:
            print("Not enough balance")

    def inquiry(self):
        print("Student name:", self.name)
        print("Balance:", self.balance)
        print("Breakfast meals:", self.breakfast)
        print("Lunch meals:", self.lunch)
        print("Dinner meals:", self.dinner)
        print("-----------------------")


# database
students = []

# functions
def add_student():
    name = input("Enter student name: ")
    balance = int(input("Enter student balance: "))
    students.append(Student(name, balance))
    print("Student added successfully")

def choose_meal():
    name = input("Enter student name: ")
    for student in students:
        if student.name == name:
            print("Choose meal:")
            print("breakfast - 200")
            print("lunch     - 500")
            print("dinner    - 250")
            meal = input("Enter meal type: ").lower()
            student.pay_meal(meal)
            return
    print("Student not found")

def inquiry_student():
    name = input("Enter student name: ")
    for student in students:
        if student.name == name:
            student.inquiry()
            return
    print("Student not found")

def monthly_report():
    print("Monthly Report")
    for student in students:
        student.inquiry()


# main loop
while True:
    print("1 - Add student")
    print("2 - Buy meal")
    print("3 - Student inquiry")
    print("4 - Monthly report")
    print("q - Quit")

    choice = input("Choose: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        choose_meal()
    elif choice == "3":
        inquiry_student()
    elif choice == "4":
        monthly_report()
    elif choice.lower() == "q":
        break
    else:
        print("Invalid choice")