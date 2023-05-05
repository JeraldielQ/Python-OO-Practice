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

    def __init__(self, start=0):
        """
        Initializes a new SerialGenerator instance.

        Start (int): The starting number of the sequence. Defaults to 0.

        """
        self.start = start
        self.current = start

    def generate(self):
        """
        Returns the next sequential number in the sequence.

        """
        result = self.current
        self.current += 1
        return result

    def reset(self):
        """
        Resets the sequence to the starting number.
        """
        self.current = self.start
