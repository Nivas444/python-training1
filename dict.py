n=int(input("how many students?"))
students={}
for i in range(n):
    name=input(f"enter name of student {i+1}:")
    mark=int(input(f"enter the mark of {name}:"))
    students[name]=mark
print(students)
highest_mark=max(students.values())
total_marks=sum(students.values())
print(f"the total marks is {total_marks}")
print(f"the highest mark is {mark} by {name}")


#emp_name=input("enter employee name:").split(",")
#print("list",emp_name)

#emp_tuple=tuple(emp_name)
#print("tuple",emp_tuple)

#emp_id=[101,102,103,104]
#emp_dict=dict(zip(emp_id,emp_name))
#print("dictionary",emp_dict)