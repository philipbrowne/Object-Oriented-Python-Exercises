"""Word Finder: finds random words from a dictionary."""
from random import choices


class WordFinder:
    """Application for finding random words from a dictionary file

    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self, file):
        self.file = open(file)
        self.words = self.wordlist(self.file)
        self.describe()

    def wordcount(self):
        return len(self.words)

    def wordlist(self, file):
        return [line.strip() for line in self.file]

    def random(self):
        return choices(self.words)[0]

    def describe(self):
        print(f'{self.wordcount()} words read')


class SpecialWordFinder(WordFinder):
    """Special Word Finder - excludes blank lines or comments
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def __init__(self, file):
        self.words = self.wordlist(file)
        super().__init__(file)

    def wordlist(self, file):
        return [line.strip() for line in file if len(line.strip().replace(' ', '')) > 0 and not line.startswith('#')]
