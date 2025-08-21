Student_Grades = {}

Tick = False
while not Tick:
    name  = input("Enter your name: ")
    grade = float(input("Enter your grade: "))
    Student_Grades[name] =  grade
    print(f"Student {name} added successfully")
    print(Student_Grades)
    Ques = input("Do you want to continue adding? Yes(Y,y)/No(N,n): ").lower()
    if Ques == "y":
        pass
    else:
        Tick = True
