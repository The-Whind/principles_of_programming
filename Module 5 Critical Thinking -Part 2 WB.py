# Ask the user to enter the number of books they purchased this month.
num_books = int(input("Enter the number of books you purchased this month: "))

# Start with 0 points.
points = 0

# Use conditional statements to determine the points based on the number of books.
if num_books == 0:
    # If the user purchased 0 books, they earn 0 points.
    points = 0
elif num_books == 2:
    # If the user purchased 2 books, they earn 5 points.
    points = 5
elif num_books == 4:
    # If the user purchased 4 books, they earn 15 points.
    points = 15
elif num_books == 6:
    # If the user purchased 6 books, they earn 30 points.
    points = 30
elif num_books >= 8:
    # If the user purchased 8 or more books, they earn 60 points.
    points = 60
else:
    # If the user purchased a number of books not specified in the criteria (like 1, 3, 5, or 7), they earn 0 points.
    points = 0

# Display the number of points awarded.
print("You have earned", points, "points this month.")

