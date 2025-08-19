StudentGrades = {}

Tick = False
while not Tick:
    name  = input("Enter your name: ")
    grade = float(input("Enter your grade: "))
    StudentGrades[name] =  grade
    print(f"Student {name} added successfully")
    print(StudentGrades)
    Ques = input("Do you want to continue adding? Y/N: ").lower()
    if Ques == "y":
        pass
    else:
        Tick = True
