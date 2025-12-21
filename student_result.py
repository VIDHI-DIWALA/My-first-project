# Student Result Calculator by Vidhi Diwala

def calculate_result():
    name = input("Enter student name: ")
    marks = []
    for i in range(5):
        mark = float(input(f"Enter marks for subject {i+1} (out of 100): "))
        marks.append(mark)
    
    total = sum(marks)
    percentage = total / 5
    
    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    print(f"
{name}'s Result:")
    print(f"Total Marks: {total}/500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

calculate_result()
