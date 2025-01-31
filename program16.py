def create_student_marks_dictionary():
    """Creates a dictionary to store student names and their marks in 5 subjects.

    Returns:
        A dictionary where keys are student names and values are dictionaries 
        containing marks for 5 subjects (subject names are keys, marks are values).
        Returns an empty dictionary if there are any issues during input.
    """

    student_marks = {}

    while True:
        student_name = input("Enter student name (or type 'done' to finish): ")
        if student_name.lower() == "done":
            break

        if not student_name:  # Check for empty input
            print("Student name cannot be empty. Please try again.")
            continue

        if student_name.lower() in (existing_student.lower() for existing_student in student_marks): #Check for duplicate entries (case-insensitive)
            print(f"Student '{student_name}' already exists in the dictionary.")
            continue

        marks = {}
        for i in range(5):  # Get marks for 5 subjects
            while True: #Input loop for marks of each subject
                try:
                    subject = input(f"Enter subject {i+1} name: ")
                    if not subject: #Check for empty input
                        print("Subject name cannot be empty. Please try again.")
                        continue

                    mark = float(input(f"Enter marks for {subject}: "))
                    if mark < 0: #Check for negative marks
                        print("Marks cannot be negative. Please try again.")
                        continue

                    marks[subject] = mark
                    break #Exit the marks input loop after valid input
                except ValueError:
                    print("Invalid input. Marks must be a number. Please try again.")

        student_marks[student_name] = marks

    return student_marks


def print_student_marks_dictionary(student_marks):
    """Prints the student marks dictionary in a formatted way.

    Args:
        student_marks: The dictionary to print.
    """

    if not student_marks:
        print("The dictionary is empty.")
        return

    print("\nStudent Marks Information:")
    for student, marks in student_marks.items():
        print(f"\n{student}:")
        for subject, mark in marks.items():
            print(f"  {subject}: {mark}")



# Create the dictionary
student_marks_dictionary = create_student_marks_dictionary()

# Print the dictionary
print_student_marks_dictionary(student_marks_dictionary)



# Example of how to access marks:
if student_marks_dictionary: #Check if dictionary is not empty before trying to access elements
    student_name_to_find = input("Enter a student name to find their marks: ")
    if student_name_to_find in student_marks_dictionary:
        print(f"\nMarks for {student_name_to_find}:")
        for subject, mark in student_marks_dictionary[student_name_to_find].items():
            print(f"  {subject}: {mark}")
    else:
        print(f"{student_name_to_find} not found in the dictionary.")