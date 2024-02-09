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
    
    if grade == "A" or int(grade)>=90:
        grade = 4
    elif grade == "B"or 90<int(grade)>=80:
        grade= 3
    elif grade == "C"or 80<int(grade)>=70:
        grade = 2
    elif grade == "D"or 70<int(grade)>=60:
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
            
