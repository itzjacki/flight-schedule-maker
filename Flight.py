from math import floor

class Flight:
    def __init__(self, flight_number, origin, destination, airplane_type):
        self.__flight_number = flight_number
        self.__origin = origin
        self.__destination = destination
        self.__airplane_type = airplane_type
        self.__distance = self.__origin.distance_to(destination)
        self.__duration = self.calculate_duration(12.5, self.__airplane_type.get_cruise_speed(), self.__distance)

    def __str__(self):
        return self.__flight_number + ": " + str(self.__origin) + " to " + str(self.__destination) + ", " + str(floor(self.__distance)) + " km, " + str(floor(self.__duration)) + " min. Aircraft: " + self.__airplane_type.get_icao()

    @staticmethod
    def calculate_duration(constant_extra, cruise_speed, distance):
        return constant_extra + distance/(cruise_speed/32.397)  # Dividing by 32.397 does knots->kilometres per minute

    def get_origin(self):
        return self.__origin

    def get_destination(self):
        return self.__destination

    def get_airplane_type(self):
        return self.__airplane_type

    def get_distance(self):
        return self.__distance

    def get_duration(self):
        return self.__duration

