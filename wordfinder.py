"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """
    A class used to read a file of words and provide a method to get a random word from the file.

    """

    def __init__(self, filename):
        """
        Initializes a new WordFinder instance and reads the words from the specified file.

        """
        self.words = self.read_file(filename)
        print(f"{len(self.words)} words read")

    def read_file(self, filename):
        """
        Reads a file of words and returns them as a list.

        """
        with open(filename) as file:
            words = [word.strip() for word in file]
        return words

    def random(self):
        """
        Returns a random word from the list of words.

        """
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """
    A subclass of WordFinder that ignores blank lines and comments in the file.

    """

    def read_file(self, filename):
        """
        Reads a file of words and returns them as a list, ignoring blank lines and comments.

        """
        with open(filename) as file:
            words = [word.strip() for word in file if word.strip()
                     and not word.startswith("#")]
        return words
