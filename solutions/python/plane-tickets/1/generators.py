"""Functions to automate Conda airlines ticketing system."""

seat_letters = 'ABCD'
seats_per_row = len(seat_letters)
def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    for i in range(number):
        yield seat_letters[i % seats_per_row]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    seat_letter_generator = generate_seat_letters(number)
    for i in range(number):
        row_number = (i // seats_per_row) + 1
        if row_number >= 13:
            row_number+=1
        yield f"{row_number}{next(seat_letter_generator)}"

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    seat_generator = generate_seats(len(passengers))
    return {name: next(seat_generator) for name in passengers}

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    code_length = 12
    for seat_number in seat_numbers:
        zero_padding = "0" * (code_length - len(seat_number) - len(flight_id))
        yield f"{seat_number}{flight_id}{zero_padding}"