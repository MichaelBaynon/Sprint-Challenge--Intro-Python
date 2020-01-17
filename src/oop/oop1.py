# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class



#base class Vehicle

class Vehicle():
    def __init__(self):
        pass

#vehicle children classes

class GroundVehicle(Vehicle):
    pass

#ground vehicle children

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass



#base class FlightVehicle

class FlightVehicle():
    def __init__(self):
        pass

# flightvehicle children

class Airplane(FlightVehicle):
    pass



#base class Starship

class Starship():
    def __init__(self):
        pass

