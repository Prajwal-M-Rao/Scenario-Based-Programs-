# Scenario 5: Online Shopping Delivery Time Estimation

# A program that estimates delivery time based on location:
# Input: Location type (1 for Local, 2 for Regional, 3 for National, 4 for International)

# Conditions:
#  for local  1 day
#  for regional  2 days
#  for national  4 days
#  for international  1 week
# Delivery Time Estimation Based on Location
print("Welcome to the Delivery Time Estimator")

location = int(input("Enter the region: \nPress 1 for Local\nPress 2 for Regional\nPress 3 for National\nPress 4 for International\n"))

if location == 1:
    print("Requires 1 day to deliver, since it's a local delivery.")
elif location == 2:
    print("Requires 2 days to deliver, since it's a regional delivery.")
elif location == 3:
    print("Requires 4 days to deliver, since it's a national delivery.")  # Fixed from 3 to 4 days
elif location == 4:
    print("Requires 1 week to deliver, since it's an international delivery.")
else:
    print("Invalid input! Please enter a number between 1 and 4.")  # Handling invalid inputs
