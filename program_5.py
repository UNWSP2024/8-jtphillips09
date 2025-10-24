# Pseudocode:
# BEGIN
# Create an empty dictionary called courses
# Display "Enter your course information below."
# Display "When finished, type 'done' for the course ID."
# REPEAT
# Prompt user to "Enter course ID (or 'done' to stop):"
# IF course ID equals 'done' (ignore case)
# EXIT loop
# ELSE
# Prompt user to "Enter course name:"
# Store the course ID and name as a key-value pair in courses
# Display "Course added!"
# UNTIL user enters 'done'
# Prompt user to "Enter a subject to search for (e.g., 'COS'):"
# Convert subject to uppercase
# Display "Courses that start with [subject]:"
# Set found = False
# FOR each course_id, course_name in courses
# IF course_id starts with subject
# Display course_id and course_name
# Set found = True
# END FOR
# IF found is False
# Display "No courses found with that subject."
# END


# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.
def course_info():
    courses = {}

    print("Enter your course information below.")
    print("When finished, type 'done' for the course ID.\n")

    # Collect course ID and course name pairs
    while True:
        course_id = input("Enter course ID (or 'done' to stop): ").strip()
        if course_id.lower() == "done":
            break
        course_name = input("Enter course name: ").strip()
        courses[course_id] = course_name
        print("Course added!\n")

    # Ask user for a subject
    subject = input("Enter a subject to search for (e.g., 'COS'): ").strip().upper()
    print(f"\nCourses that start with '{subject}':\n")

    found = False
    for course_id, course_name in courses.items():
        if course_id.upper().startswith(subject):
            print(f"{course_id}: {course_name}")
            found = True

    if not found:
        print("No courses found with that subject.")

# Run the program
course_info()
