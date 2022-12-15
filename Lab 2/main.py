import staff

log = open("log.txt", 'w')

employee = staff.Employee("Vladimir Bezukh", 22, "Student")

# save
employee.save("employee_data.json")
log.write(f"Saved information\n"
          f"{employee}\n"
          f"\n")

# change
employee.reposition("Python programmer")
log.write(f"Change of position\n"
          f"{employee}\n"
          f"\n")

# load
employee.load("employee_data.json")
log.write(f"Loaded information\n"
          f"{employee}\n")
