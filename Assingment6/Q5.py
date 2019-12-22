class : car
attributes : year, mpg and speed
object : car1 (car2,car3.car4,car5)

first method:

# Creates class Car
class Car:

    # create class attributes
    name = "c200"
    make = "mercedez"
    model = 2008
    mgp = 100
    accelerate= 20

    # create class methods
    def start(self):
        print ("Engine started")

    def stop(self):
        print ("Engine switched off")

# Creates car_a object of Car class
car_a = Car()

# Creates car_b object of car class
car_b = Car()



car_b.start()

print(car_b.model)
print(car_b.name)
print(car_b.make)
print(car_b.mgp)
print(car_b.accelerate)

Methods
(1) Static Methods:
===================


class Car:

    @staticmethod
    def get_class_details():
        print ("This is a car class")

Car.get_class_details()


(2) The str Method:
===================

# Creates class Car
class Car:

    # create class methods

    def __str__(self):
        return "Car class Object"

    def start(self):
        print ("Engine started")

car_a = Car()
print(car_a)


(3) Constructors:
==================

class Car:

    # create class attributes
    car_count = 0

    # create class methods
    def __init__(self):
        Car.car_count +=1
        print(Car.car_count)
        
        car_a = Car()
car_b = Car()
car_c = Car()



