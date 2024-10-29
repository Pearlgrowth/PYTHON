def calculate_grade(physics, math, kiswahili):
    # Error Handling: Check for negative marks
    if physics < 0 or math < 0 or kiswahili < 0:
        return "Error: Marks cannot be negative."

    # Calculate the average
    total = physics + math + kiswahili
    average = total / 3

    # Error Handling: Check if average is realistic
    if average > 100:
        return "Error: The average mark is greater than 100, please check the marks entered."

    # Assign Grades based on the average
    if average >= 70:
        grade = 'A'
    elif average >= 60:
        grade = 'B'
    elif average >= 50:
        grade = 'C'
    elif average >= 40:
        grade = 'D'
    else:
        grade = 'F'

    # Return average and grade
    return f"Average Mark: {average:.2f}, Grade: {grade}"


# Example usage
result = calculate_grade(85, 78, 90)
print(result)
