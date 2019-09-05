class AirplaneType:
    def __init__(self, name, iata, icao, runway_requirement, cruise_speed, seat_amount, turnaround_time):
        self.__name = name
        self.__iata = iata
        self.__icao = icao
        self.__runway_requirement = runway_requirement  # In metres
        self.__cruise_speed = cruise_speed  # In knots
        self.__seat_amount = seat_amount
        self.__turnaround_time = turnaround_time  # In minutes

    def get_name(self):
        return self.__name

    def get_iata(self):
        return self.__iata

    def get_icao(self):
        return self.__icao

    def get_cruise_speed(self):
        return self.__cruise_speed

    def get_seat_amount(self):
        return self.__seat_amount

    def can_use(self, airport):
        return airport.get_runway_length() >= self.__runway_requirement

