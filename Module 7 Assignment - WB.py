# Step 1: Create dictionaries

course_rooms = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

course_instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

course_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Step 2: Prompt the user to enter a course number
course_number = input("Enter a course number (e.g., CSC101): ")

# Step 3: Retrieve and display the course details
if course_number in course_rooms:
    room = course_rooms[course_number]
    instructor = course_instructors[course_number]
    time = course_times[course_number]

    print(f"Course Number: {course_number}")
    print(f"Room Number: {room}")
    print(f"Instructor: {instructor}")
    print(f"Meeting Time: {time}")
else:
    print("Course number not found.")

