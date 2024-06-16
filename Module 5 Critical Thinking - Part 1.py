# Ask the user for the number of years they want to track rainfall for.
num_years = int(input("Enter the number of years you want to track rainfall for: "))

# Starting with zero total rainfall and zero total months.
total_rainfall = 0
total_months = 0

# We're going to loop through each year now.
for year in range(num_years):
    print("Year", year + 1)  # This shows which year we're on.

    # Inside each year, we're going to loop through each of the 12 months.
    for month in range(12):
        # Ask the user for the rainfall amount for the current month.
        rainfall = float(input("Enter the inches of rainfall for month " + str(month + 1) + ": "))
        # Add the current month's rainfall to the total rainfall we've been tracking.
        total_rainfall += rainfall
        # Add 1 to our count of total months.
        total_months += 1

# Now that we have all the data, let's calculate the average rainfall per month.
average_rainfall = total_rainfall / total_months

# Finally, let's print out the results:
print("Number of months:", total_months)  # Total number of months we tracked.
print("Total inches of rainfall:", round(total_rainfall, 2))  # Total rainfall over all those months.
print("Average rainfall per month:", round(average_rainfall, 2))  # Average rainfall per month.

