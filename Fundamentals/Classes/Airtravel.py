class Flight:
    """A Flight with a particular passenger aircraft."""
    #   IT IS NOT THE CONSTRUCTOR
    #   IT INITIALIZES AN OBJECT THAT HAS ALREADY BEEN INITIALIZED

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No code")

        if not number[:2].isupper():
            raise ValueError("No valid code")

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("invalid route number")

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def aircraft_seatingPlan(self):
        return self._aircraft.model()

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger.

        Args:
            seat: A seat designator such as '12c' or '21f'.
            passengenger: The passenger name.

        Raises:
            ValueError: If the seat is unavailable.
        """
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid sear row {}".format(row_text))

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
        return (range(1, self._num_rows + 1), "ABCDEFGJHK"[:self._num_seats_per_row])


if(__name__ == "__main__"):
    from pprint import pprint as pp

    f = Flight("BA750", Aircraft("G-EUPT", "Airbus A319", 22, 6))
    f.number()
    f.airline()
    f.aircraft_model()

    pp(f._seating)

    f.allocate_seat('1C', 'Flavio Pegas')
    f.allocate_seat('1C', 'Flavio Pegas')
    f.allocate_seat('15F', 'Jonas')
    f.allocate_seat('33F', 'Papa')