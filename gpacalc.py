## basically easy way to calculate gpa real quick
#grade*ID = gradepoints ---> gradepoints/credits
gradepoints = 0
credits = 0
while True:
    courseID = input("Enter the Course # or say 'done' if you are finished > ")

    # str(courseID[1])

    if courseID == "done":
        break

    grade = input("What was the letter grade in your class > ")
    
    if grade == "A":
        grade = 4
    elif grade == "B":
        grade= 3
    elif grade == "C":
        grade = 2
    elif grade == "D":
        grade = 1
    else:
        print("please enter a letter grade correctly")
        continue

    times = int(courseID[1]) * grade
    # gpa = gradepoints/credits

    #change this to else statement, make if statements for errors
    gradepoints += times
    credits += int(courseID[1])

if credits != 0:
    gpa = gradepoints/credits
    print("GPA > ", gpa)

else:
    print("No classes were input, try again")
            
