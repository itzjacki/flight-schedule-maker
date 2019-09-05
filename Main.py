from codecs import open as codecs_open

from Airport import Airport
from AirplaneType import AirplaneType
from Flight import Flight



def populate_airport_list(file_name):
    airport_list = []
    airport_file = codecs_open(file_name, "r", "utf8")
    for line in airport_file:
        # Format for data:
        # Name | IATA | ICAO | RWY length | Domestic tfc/day | GPS latitude | GPS Longitude
        s = line.split("|")
        airport_list.append(Airport(s[0], s[1], s[2], int(s[3]), int(s[4]), (float(s[5]), float(s[6]))))
    airport_file.close()
    return airport_list


def main():
    # Populates airport list with data from text file
    airport_list = populate_airport_list("AirportData.txt")
    print(len(airport_list), "airports imported.")

    # --- All code below this line is highly temporary and is only used to test ---

    # Create temporary plane
    dh8 = AirplaneType("DeHavilland Canada DHC-8-400", "DH4", "DH4D", 1289, 345, 79, 30)

    fnr_counter = 100

    flight_list = []
    for origin in airport_list:
        for destination in airport_list:
            if origin != destination \
                    and origin.distance_to(destination) < 800\
                    and (origin.get_daily_passengers() > 250 or destination.get_daily_passengers() > 250) \
                    and ((origin.get_daily_passengers() > 250 and destination.get_daily_passengers() > 250 and origin.distance_to(destination) > 150) or origin.distance_to(destination) < 250)\
                    and dh8.can_use(origin) and dh8.can_use(destination):

                fnr = "WF" + str(fnr_counter)
                fnr_counter += 1
                flight_list.append(Flight(fnr, origin, destination, dh8))

    f = open("output.txt", "w")
    f.truncate(0)
    test_list = set()
    for flight in flight_list:
        print(flight)
        f.write(str(flight) + "\n")
        if flight.get_origin() not in test_list:
            test_list.add(flight.get_origin())
    print(len(flight_list), "flights created.")
    print(len(test_list), "airports covered.")
    f.close()


main()

