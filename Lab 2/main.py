import staff

employee = staff.Employee("Vladimir Bezukh", 22, "Student")

# save
employee.save("employee_data.json")
print("Saved information:")
employee.print()

# change
employee.reposition("Python programmer")
print("\nChange of position:")
employee.print()

# load
employee.load("employee_data.json")
print("\nLoaded information:")
employee.print()
