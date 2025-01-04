# 1. Student Grade Calculator
# Objective: Build a program to calculate grades for students based on marks entered.
# Steps:
# 1. Ask the user to input marks for 5 subjects.
# 2. Validate that the input is a number and within a valid range (0-100).
# 3. Calculate the total marks and percentage.
# 4. Assign grades based on percentage:
# o 90% and above: A+
# o 80%-89%: A
# o 70%-79%: B
# o 60%-69%: C
# o Below 60%: Fail.
# 5. Display the total marks, percentage, and grade. 

# Function to calculate grade
def Show_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "Fail"

# Main function to calculate grades
def calculate_grade():
    subjects = []
    marks = []
    total_marks = 0
    n=int(input("Enter the number of subjects: "))

    # Input subject names and marks
    for i in range(n):
        sub = input(f"Enter subject name {i+1}: ")
        # Truncate long subject names
        if len(sub) > 20:
            sub = sub[:17] + "..."  # Keep 17 characters + "..."
        subjects.append(sub)
        while True:
            try:
                mark = int(input(f"Enter marks of {sub} (0-100): "))
                if mark < 0 or mark > 100:
                    print("Marks should be between 0 and 100. Please try again.")
                else:
                    marks.append(mark)
                    break
            except ValueError:
                print("Invalid input. Please enter a valid Mark.")

    # Calculate total marks and percentage
    for i in marks:
        total_marks += i
    percentage = (total_marks / (n*100)) * 100

    # Calling function to get grade
    grade = Show_grade(percentage)

    # Displaying results
    print("\nResults:")
    print("-"*40)
    print(f"|{'Subject':<20} | {'marks':>8}|")
    print("-"*40)
    for i in range(n):
        print(f"|{subjects[i]:<20} |{marks[i]:>8} |")
    print("-"*40)    
    print(f"Total Marks: {total_marks}\nPercentage: {percentage:.2f}%")
    print("-"*40)
    print(f"Grade: {grade}")

    #For Dispalying Grade Comments
    print("-"*40)
    print("Remark :")
    if grade == "A+":
        print("Excellent performance! You scored above 90%.")
    elif grade == "A":
        print("Great performance! You scored between 80-89%.")
    elif grade == "B":
        print("Good performance! You scored between 70-79%.")
    elif grade == "C":
        print("Fair performance! You scored between 60-69%.")
    else:
        print("You need to improve. You scored below 60%.")

# Run the program
calculate_grade()
