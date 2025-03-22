# Scenario 4: Travel Booking with Discounts

# A travel agency offers discounts based on destination and mode of transport:

# Input: destination type and type of ticket

# Conditions:
# If the destination is international:
# If flying first class, give a 15% discount.
# If economy, give a 10% discount.
# If the destination is domestic:
# No discount for economy.
# 5% discount for first class.

print("Welcome to Pravaasa - Your Travel Booking Assistant")

des_type = int(input("Enter your destination type:\n1. International\n2. Domestic\n"))

if des_type == 1:
    print("You have chosen an International Destination.")

    mode = int(input("Enter your flight class:\n1. First Class\n2. Economy\n"))

    if mode == 1:
        print("Great choice! You’ll receive a 15% discount.")
    elif mode == 2:
        print("You’ll receive a 10% discount.")
    else:
        print("Invalid choice! Please enter 1 for First Class or 2 for Economy.")

elif des_type == 2:
    print("You have chosen a Domestic Destination.")

    # Get user input for ticket type
    mode = int(input("Enter your flight class:\n1. First Class\n2. Economy\n"))

    if mode == 1:
        print("Nice! You’ll receive a 5% discount.")
    elif mode == 2:
        print("Sorry, no discount is available for Economy class.")
    else:
        print("Invalid choice! Please enter 1 for First Class or 2 for Economy.")

else:
    print("Invalid destination type! Please enter 1 for International or 2 for Domestic.")
