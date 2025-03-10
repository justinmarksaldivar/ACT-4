def assign_grade():
    marks = int(input("What is your Grade?"))
    if marks <= 0:
        print("Invalid score!")
    if marks >= 101:
        print("Invalid score!")
    elif marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
        
assign_grade()