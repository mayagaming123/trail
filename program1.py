def calculate_average_and_grade(marks):
    """Calculates the average and assigns a grade based on the average.

    Args:
        marks: A list of numerical marks.

    Returns:
        A tuple containing the average and the grade (string), or an error message if the input is invalid.
    """

    if not marks:  # Check for empty list
        return "No marks provided.", None

    if not all(isinstance(mark, (int, float)) and 0 <= mark <= 100 for mark in marks):  # Input validation
        return "Invalid marks. Marks must be numbers between 0 and 100.", None

    average = sum(marks) / len(marks)

    grade = assign_grade(average)  # Assign the grade
    return average, grade


def assign_grade(average):
    """Assigns a letter grade based on the average.

    Args:
        average: The average mark.

    Returns:
        The letter grade (string).
    """
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# Get input from the user (or set marks directly)
try:
    marks_input = input("Enter marks separated by spaces: ")
    marks_str = marks_input.split()

    if not marks_str: #check if user give empty input
      marks = []
    else:
      marks = [float(mark) for mark in marks_str]  # Convert strings to floats

    average, grade = calculate_average_and_grade(marks)

    if isinstance(average, str): #check if any error message is there
      print(average) #print error message
    else:
      print("Marks:", marks)
      print(f"Average: {average:.2f}")  # Format average to 2 decimal places
      print("Grade:", grade)

except ValueError:
    print("Invalid input. Please enter numbers only.")

# Example usage (without user input)
marks = [85, 92, 78, 65, 95]
average, grade = calculate_average_and_grade(marks)
print("\nExample Usage:")
print("Marks:", marks)
print(f"Average: {average:.2f}")
print("Grade:", grade)


marks = [55, 45, 60, 70, 50]
average, grade = calculate_average_and_grade(marks)
print("\nExample Usage:")
print("Marks:", marks)
print(f"Average: {average:.2f}")
print("Grade:", grade)

marks = [] #empty list
average, grade = calculate_average_and_grade(marks)
print("\nExample Usage:")
print("Marks:", marks)
print(average) #print error message
print("Grade:", grade) #print None

marks = [55, 'a', 60, 70, 50] #list with string
average, grade = calculate_average_and_grade(marks)
print("\nExample Usage:")
print("Marks:", marks)
print(average) #print error message
print("Grade:", grade) #print None