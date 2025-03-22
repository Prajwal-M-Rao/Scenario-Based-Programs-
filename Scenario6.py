# Scenario 6: Age-Based Ticket Pricing

# A theme park charges ticket prices based on age and group discounts:

# Conditions:
# If the person is a child (age < 12):
# If in a group, ticket is free.
# Otherwise, charge $10.
# If the person is an adult:
# If in a group, apply a 20% discount on $20.
# Otherwise, charge $20.

print("WELCOME to BOMMI's Theme Park")

# Get user age input
age = int(input("Please enter your age: "))

if 0< age < 12:
    print("Are you entering as part of a group?")
    press = int(input("Press 1 for 'Yes' or 2 for 'No': "))
    if press == 1:
        print("Congrats! Your ticket is free.")
    elif press == 2:
        print("Please pay $10.")
    else:
        print("Invalid choice. Please enter 1 or 2.")
elif 12 <= age <60:
    print("Are you entering as part of a group?")
    press = int(input("Press 1 for 'Yes' or 2 for 'No': "))
    if press == 1:
        print("Congrats! You got a 20% discount on $20.")
        print("The fare is $16.")
    elif press == 2:
        print("Please pay $20.")
    else:
        print("Invalid choice. Please enter 1 or 2.")
else:
    print("Enter a valid age")