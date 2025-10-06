class Student:
    def __init__(self):
        self.roll = input("Enter the roll: ")
        self.name = input("Enter the name: ")
        self.marks = []
        n = int(input("Enter the number of marks: "))
        for i in range(n):
            mark = int(input(f"Enter mark {i+1}: "))
            self.marks.append(mark)
    def write(self):
        print(f"Name: {self.name}")
        print(f"Rollno: {self.roll}")
        print(f"Marks: {self.marks}")
        print("Total:", sum(self.marks))
        print("Average:", sum(self.marks)/len(self.marks))

s1 = Student()
s1.write()