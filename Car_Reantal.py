#Car Rental Service

'''Scenario:
A car rental company needs a system to register and rent cars.

Question:
Write a program that:

  Creates a Car class with attributes: carModel, rentalPrice, and isAvailable.
  Implements a method rentCar() that sets isAvailable = False.
  Implements a method returnCar() that sets isAvailable = True.
  Creates an object and simulates a car rental process.'''

class Car:
    def __init__(self,carModle,rentalPrize,isAvailable):
        self.carModel=carModle
        self.rent=rentalPrize
        self.isAvailable=isAvailable

    def rentCar(self):
        if self.isAvailable:
            print("The car is now being rented\nRent Price:", self.rent)
            print("\n")
            self.isAvailable = False
        else:
            print("Sorry, this car is not available for rent.")

    def returnCar(self):
        if not self.isAvailable:
            print("The car has been returned\nThank You!!!")
            self.isAvailable = True
        else:
            print("This car was not rented.")

c1=Car("Maruthi800",750,True)
c2=Car("Bugatti",100000,False)
c3=Car("Rolls Royce",800000,True)
c4=Car("BMW",50000,True)

cars={"Maruthi800":c1, "Bugatti":c2, "Rolls Royce": c3, "BMW":c4}

while(True):
    print("Welcome to CAR car Rentals:\n")
    print("Cars \n\tMaruthi800\n\tBugatti\n\tRolls Royce\n\tBMW\nExit")
    print("Please select the car model")
    model=input().strip()
    if model.lower()=='exit':
        print("Thank you!!  Visit Again")
        exit()

    elif model in cars:
        car=cars[model]
        print("1.Rent the car\n2.Return the car\n3.Exit")
        opt=int(input())
        if opt == 1:
            car.rentCar()
        elif opt==2:
            car.returnCar()
        else:
            exit()
    else:
        print("Model not found")
        exit()