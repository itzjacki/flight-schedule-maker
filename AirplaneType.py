class AirplaneType:
    def __init__(self, name, iata, icao, runway_requirement, seat_amount):
        self.__name = name
        self.__iata = iata
        self.__icao = icao
        self.__runway_requirement = runway_requirement
        self.__seat_amount = seat_amount

    def get_name(self):
        return self.__name

    def get_iata(self):
        return self.__iata

    def get_icao(self):
        return self.__icao

    def get_seat_amount(self):
        return self.__seat_amount

    def can_land(self, airport):
        return airport.get_runway_length() >= self.__runway_requirement

