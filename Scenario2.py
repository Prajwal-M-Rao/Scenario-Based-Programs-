#Scenario 2: Banking Transaction

#Write a program to simulate a withdrawal from a bank account:
#Input: Current balance and withdrawal amount
# Conditions:
# If the withdrawal amount is less than or equal to the balance, allow the transaction and display the
# remaining balance.
# If the withdrawal amount exceeds the balance, display "Insufficient funds."


print("Welcome to BOMMI's Bank")

while True:
    balance = int(input("Enter your current bank account balance: "))
    if balance >= 0:
        break
    else:
        print("Invalid amount! Please enter a valid balance (≥ 0).")

while True:
    withdrawal = int(input("Enter the amount you want to withdraw: "))
    if withdrawal > 0:
        break
    else:
        print("Invalid amount! Please enter a positive withdrawal amount.")

if withdrawal <= balance:
    print("Transaction successful!")
    remaining = balance - withdrawal
    print(f"Remaining balance: ${remaining}")
else:
    print("Insufficient funds! Transaction declined.")
