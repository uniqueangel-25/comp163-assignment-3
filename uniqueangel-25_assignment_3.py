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

elif choice == "B": 
    if current_gpa >= 3.0:
        study_hours += 6 
        stress_level -= 6
    else: 
        study_hours += 6 
        stress_level += 6

elif choice == "C":
    if current_gpa >= 3.5: 
        study_hours += 8 
        stress_level -= 8
    else: 
        study_hours += 8 
        stress_level += 8
   
else: 
    print("Invalid input")
    study_hours += 7
    stress_level += 10

Study_options = ["Programming", "Math", "English", "History"]
print("Choose your study focus from:", Study_options)
Subject =  input("Enter subject:")

if Subject not in Study_options or Subject == "": 
    print("Invalid Subject")

else: 
    if Subject == "Programming":
        current_gpa += 0.2 
        social_points -= 5 
        stress_level += 3
    elif Subject == "Math":
        current_gpa += 0.3
        social_points -= 4
        stress_level += 3
    
    elif Subject == "English":
        current_gpa += 0.1 
        social_points += 5 
        stress_level -= 2
    elif Subject == "History":
        current_gpa += 0.4
        social_points += 3
        stress_level -= 4


print("Your GPA is: ", round(current_gpa), 2)
print("Your study hours:",study_hours)
print("Your social points:",social_points)
print("Your stress level:",stress_level, "\n")

print("Final Assessment")
if type(current_gpa) is float:
    if current_gpa >= 3.5:
        if stress_level <= 50 and social_points >= 40:
            Ending = "Graduated with honors and balanced life"
        elif stress_level > 70:
            Ending = "High GPA but burnout"
        else:
            Ending = "Graduated but less social"
    elif current_gpa >= 2.0:
        if social_points >= 60:
            Ending = "Average grades but good life"
        else:
            Ending = "Finished with steady progress"
    else:
        Ending = "Faild to maintain academic standing"
elif type(current_gpa) is not float: 
    Ending = "Error"

print("\n" + Ending)
print("Your GPA is: ", round(current_gpa), 2)
print("Your study hours:",study_hours)
print("Your social points:",social_points)
print("Your stress level:",stress_level, "\n")

