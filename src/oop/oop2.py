# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels

    def drive(self):
        return 'vroooom'

    def __str__(self):
        return f'I am a Ground Vehicle with {self.num_wheels} wheels'


myGroundVehicle = GroundVehicle()
print(myGroundVehicle.drive())
print(myGroundVehicle.__str__())


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels=2):
        super().__init__(num_wheels=num_wheels)

    def drive(self):
        return 'BRAAAP!!'

    def __str__(self):
        return f'I am a Motorcycle with {self.num_wheels} wheels'

myMotorcycle = Motorcycle()
print(myMotorcycle.drive())
print(myMotorcycle.__str__())

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

result = [i.drive() for i in vehicles]
print(result)
