"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        self.num = start
        self.start = start

    def __repr__(self):
        return f"Serial(start={self.start} next={self.start+1})"

    def generate(self):
        """Returns the next sequential number in increments of one and changes the current number"""
        self.num += 1
        return self.num - 1

    def reset(self):
        """Resets the current number to the original start value"""
        self.num = self.start
