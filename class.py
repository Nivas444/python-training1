class student:
    def read(self):
        self.name = input("Enter the student name: ")
        self.marks = []
        for i in range(3):
            mark = int(input(f"Enter mark {i+1}: "))
            self.marks.append(mark)
    def write(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Total:", sum(self.marks))

s1 = student()
s1.read()
s1.write()

        
