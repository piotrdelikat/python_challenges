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

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger.

        :arg
            seat: A seat designator such as '12C' or '21F'.
            passenger: The passenger name.

        :raises
            ValueError: If the seat is unavailable.
        """

        #assign a passanger name to the number in seating plan
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))

        if row not in rows:
            raise ValueError("Invalid row number {}".format(row))

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))

        self._seating[row][letter] = passenger

class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows +1),
                "ABCDEFGHJK"[:self._num_seats_per_row])
