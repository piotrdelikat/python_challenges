"""Demonstrate interaction with refrigerator."""

from contextlib import closing


class FridgeRide:
    """Simulate interaction with a fridge"""

    def open(self):
        print("Open fridge door.")

    def take(self, food):
        print("Finding {}...".format(food))
        if food == 'bacon':
            raise RuntimeError("Health warning!")
        print("Taking {}".format(food))

    def close(self):
        print("Close fridge door.")


def eat(food):
    with closing(FridgeRide()) as r:
        r.open()
        r.take(food)


#context manager with func: closing will always make shure to close the operation