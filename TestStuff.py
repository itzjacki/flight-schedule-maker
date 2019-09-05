from Airport import Airport
from AirplaneType import AirplaneType
from Flight import Flight
from random import randint

airport_trf = Airport("Sandefjord Lufthavn Torp", "TRF", "ENTO", 2989, 44384, (59.1866, 10.2586))
airport_trd = Airport("Trondeim Lufthavn Værnes", "TRD", "ENVA", 2999, 448763, (63.4575, 10.9241))
airport_bgo = Airport("Bergen Lufthavn Flesland", "BGO", "ENNR", 2990, 528600, (60.2936, 5.2180))
airport_svg = Airport("Stavanger Lufthavn Sola", "SVG", "ENZV", 2556, 358113, (58.876667, 5.637778))
airport_osl = Airport("Oslo Lufthavn Gardermoen", "OSL", "ENGM", 3600, 1502223, (60.202778, 11.083889))

airport_list = [airport_trd, airport_trf, airport_bgo, airport_svg, airport_osl]

# print(airport_trd)
# print(airport_trf)
# print(airport_bgo)
# print(airport_svg)

dh8 = AirplaneType("DeHavilland Canada DHC-8-400", "DH4", "DH4D", 1289, 345, 79, 30)

# flight_1 = Flight("WF487", airport_trf, airport_trd, dh8)
# print(flight_1)

flight_list = []
flight_numbers_taken = []  # TODO: Rewrite flight number generation system

for origin in airport_list:
    for destination in airport_list:
        if origin != destination:
            while True:
                flight_number = "WF" + str(randint(100, 999))
                if flight_number not in flight_numbers_taken:
                    break
            flight_list.append(Flight(flight_number, origin, destination, dh8))

for flight in flight_list:
    print(flight)
print("In total " + str(len(flight_list)) + " flights")
