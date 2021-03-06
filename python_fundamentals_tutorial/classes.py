"""Model for aircraft flights"""


class Flight:
    """A flight with a particular passenger aircraft."""

    def __init__(self, number, aircraft):
        # class invariants
        if not number[:2].isalpha():
            raise ValueError("No arline code in '{}'".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid arline code '{}'".format(number))

        if not (number[2:]).isdigit() and int(number[2:]) <= 9999:
            raise ValueError("Invalid route number '{}'".format(number))

        self._number = number
        # _number as we don't want to clash into number() method
        # it's also an convention preventing from overriding initial values
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter:None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def arline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def _parse_seat(self, seat):
        """Parse a seat designator into a valid row and letter.

        :arg
            seat: A seat designator such as '12C' or '21F'.

        :returns
            A tuple containing an integer and a string for row and seat.
        """
        row_numbers, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))

        if row not in row_numbers:
            raise ValueError("Invalid row number {}".format(row))

        return row, letter

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger.

        :arg
            seat: A seat designator such as '12C' or '21F'.
            passenger: The passenger name.

        :raises
            ValueError: If the seat is unavailable.
        """
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))

        self._seating[row][letter] = passenger

    def relocate_passenger(self, from_seat, to_seat):
        """Relocate passenger to a different seat.

        :arg
            from_seat: The existing seat designator for the passenger to be moved

            to_seat: The new seat designator.
        """

        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger to relocate in the seat {}".format(from_seat))

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} already occupied".format(to_seat))

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        """An iterable series of passenger seating allocations."""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, "{}{}".format(row, letter))


class Aircraft:

    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


class AirbusA319(Aircraft):

    def model(self):
        return "AirbusA319"

    def seating_plan(self):
        return range(1, 23), "ABCDEF"


class Boeing777(Aircraft):

    def model(self):
        return "Boeing777"

    def seating_plan(self):
        return range(1, 56), "ABCDEGHJK"


def make_flights():
    f = Flight("BE759", AirbusA319("G-EFTP"))
    f.allocate_seat('12A', 'Rickey Martin')
    f.allocate_seat('15F', 'Amber Doom')
    f.allocate_seat('15E', 'Max Pain')
    f.allocate_seat('1C', 'George Smith')
    f.allocate_seat('1D', 'Raul Sam Junior')

    g = Flight("AR56", Boeing777("F-GPRS"))
    g.allocate_seat('3G', 'Norma Dorn')
    g.allocate_seat('33K', 'Richard Rich')
    g.allocate_seat('15B', 'Marcel Haisa')
    g.allocate_seat('11C', 'Xio Ambauta')

    return f, g


# You are not compelled to create classes without good reason
def console_card_printer(passenger, seat, flight_number, aircraft):
    output = "| Name: {0}"      \
             "  Flight: {1}"    \
             "  Seat: {2}"      \
             "  Aircraft: {3}"  \
             " |".format(passenger, flight_number, seat, aircraft)
    banner = '+' + '-' * (len(output) - 2) + '+'
    border = '|' + ' ' * (len(output) - 2) + '|'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()