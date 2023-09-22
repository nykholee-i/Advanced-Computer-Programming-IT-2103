# function to calculate the average grade
def calculate_average(grades):
    total = sum(grades)
    average = total / len(grades)
    return average

# list for the subjects ganorn
subjects = ["English", "Filipino", "Science", "Math", "Araling Panlipunan", "Physical Education"]
grades = []

# input grades for each subject
for subject in subjects:
    while True: #conditional eme eme
        try:
            grade = float(input(f"Enter your {subject} grade: "))
            if 0 <= grade <= 100:
                grades.append(grade)
                break
            else:
                print("Invalid grade. Please enter a grade between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric grade.")

# calculate the average grade
average_grade = calculate_average(grades)

# display or print the results
print("\nYour Grades:")
for i in range(len(subjects)):
    print(f"{subjects[i]}: {grades[i]}")

print(f"\nAverage Grade: {average_grade:.2f}")
