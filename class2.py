class Student:
    def __init__(self):
        self.roll = None
        self.name = None
        self.marks = []
    def access(self):
        self.roll = input("Enter the roll: ")
        self.name = input("Enter the name: ")
        self.marks = []
        n = int(input("Enter the number of marks: "))
        for i in range(n):
            mark = int(input(f"Enter mark {i+1}: "))
            self.marks.append(mark)
    def display(self):
        if self.name is None or self.roll is None or not self.marks:
            print("No student data available. Please use Access first.")
            return
        print(f"Name: {self.name}")
        print(f"Rollno: {self.roll}")
        print(f"Marks: {self.marks}")
        print("Total:", sum(self.marks))
        print("Average:", sum(self.marks)/len(self.marks) if self.marks else 0)
    def update(self):
        if self.name is None or self.roll is None:
            print("No student data to update. Please use Access first.")
            return
        new_name = input("Enter the new name: ")
        new_roll = input("Enter the new roll: ")
        self.roll = new_roll
        self.name = new_name
        print("Name updated successfully.")
    def delete(self):
        self.roll = None
        self.name = None
        self.marks = []
        print("Record deleted successfully.")

s1 = Student()
while True:
    print("\n1. Access\n2. Display\n3. Update\n4. Delete\n5. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    if choice == 1:
        s1.access()
    elif choice == 2:
        s1.display()
    elif choice == 3:
        s1.update()
    elif choice == 4:
        s1.delete()
    elif choice == 5:
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")