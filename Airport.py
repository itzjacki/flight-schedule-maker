from math import radians, asin, sin, cos, sqrt


class Airport:
    def __init__(self, name, iata, icao, runway_length, daily_passengers, position, turnaround_factor=1.0):
        self.__name = name
        self.__iata = iata
        self.__icao = icao
        self.__runway_length = runway_length  # Used to see if certain plane type can land on runway, in metres
        self.__daily_passengers = daily_passengers  # Amount of outgoing passengers from airport
        self.__position = position  # Tuple with Decimal Degree GPS coordinates, e.g. (50.010, -119.800)
        self.__turnaround_factor = turnaround_factor  # Extra time usually taken in turnaround due to traffic/other. 1.0 is standard, which means no notable delay because of the airport. 1.10 means the turnaround takes 10% longer than normal.

    def __str__(self):
        return self.get_name() + " (" + self.get_iata() + ")"

    def get_name(self):
        return self.__name

    def get_iata(self):
        return self.__iata

    def get_icao(self):
        return self.__icao

    def get_runway_length(self):
        return self.__runway_length

    def get_daily_passengers(self):
        return self.__daily_passengers

    def get_position(self):
        return self.__position

    def get_turnaround_factor(self):
        return self.__turnaround_factor

    def distance_to(self, airport):
        # Returns great circle distance between two airports, in kilometres
        lat1 = self.get_position()[0]
        lon1 = self.get_position()[1]
        lat2 = airport.get_position()[0]
        lon2 = airport.get_position()[1]

        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

        return 2 * 6371 * asin(sqrt(sin((lat2 - lat1)/2) ** 2 + cos(lat1) * cos(lat2) * sin((lon2 - lon1)/2) ** 2))
