# E-commerceProductSystem
#
#  Scenario:
#  An e-commercecompany needs a Productclass for onlineshopping.
#
#  Question:
#  Writeaprogramthat:
#   Creates a Product class with attributes productId,productName,and price.
#   Defines a parameterized constructor to initialize these values.
#   Implements a method applyDiscount(floatpercentage) to reduce the price based on the discount.
#   Creates an object,applies a discount,and displays the updatedprice

class Product:
    def __init__(self, pid, pname, price):
        self.pid = pid
        self.pname = pname
        self.price = price

    def applyDiscount(self, percentage):
        print("Original Price:", self.price)

        # Calculate the discount amount correctly
        discount_amount = self.price * (percentage / 100)
        updated_price = self.price - discount_amount
        print("New Price after Discount:", updated_price)

        # Update the price
        self.price = updated_price
        return updated_price

p1 = Product(1, "Car", 2500000)
p2 = Product(2, "Bike", 800000)
p3 = Product(3, "Bus", 10000000)

print("Enter the product req:\n1.Car\n2.Bike\n3.Bus")
pid = int(input())

if pid == 1:
    print("You have selected the Car")
    print("Enter the discount percentage")
    discount = float(input())
    p1.applyDiscount(discount)
elif pid == 2:
    print("You have selected the Bike")
    print("Enter the discount percentage")
    discount = float(input())
    p2.applyDiscount(discount)
elif pid == 3:
    print("You have selected the Bus")
    print("Enter the discount percentage")
    discount = float(input())
    p3.applyDiscount(discount)
else:
    print("Sorry not available")