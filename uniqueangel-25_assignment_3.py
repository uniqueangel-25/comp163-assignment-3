student_name = "Angel"
current_gpa = 3.4
study_hours = 20
social_points = 50
stress_level = 80

print("Welcome! Your name is",student_name)
print("Your stats are as followed:")
print("Your GPA is:",current_gpa)
print("Your study hours:",study_hours)
print("Your social points:",social_points)
print("Your stress level:",stress_level, "\n")

print("Choose your course load:")
print("A) Light (12 credits)")  
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")
choice = input("Your choice: ")


if choice == "A": 
    if current_gpa >= 2.0: 
        study_hours += 5 
        stress_level -= 5 
    else: 
        study_hours += 2 
        stress_level += 5

    # Use comparison operators to check GPA and adjust variables
elif choice == "B": 
    if current_gpa >= 3.0:
        study_hours += 6 
        stress_level -= 6
    else: 
        study_hours += 6 
        stress_level += 6
    # Different logic path
elif choice == "C":
    if current_gpa >= 3.5: 
        study_hours += 8 
        stress_level -= 8
    else: 
        study_hours += 8 
        stress_level += 8
    # Heavy load - check if GPA >= 3.5 for different outcomes
else: 
    print("Invalid input")
    study_hours += 7
    stress_level += 10
    # Handle invalid input

Study_options = ["Programming", "Math", "English", "History"]
print("Choose your study focus from:", Study_options)
Subject =  input("Enter subject:")
if Subject in Study_options: 
    if Subject in ["Programming", "Math"]:
        current_gpa += 0.2
        social_points -= 5
        stress_level += 3
    elif Subject in ["English", "History"]:
        current_gpa += 0.1
        social_points += 5
        stress_level -= 2
        pass
else:
    print("Invalid Subject")
print("Your GPA is: ", round(current_gpa), 2)
print("Your study hours:",study_hours)
print("Your social points:",social_points)
print("Your stress level:",stress_level, "\n")
    # Handle invalid input
