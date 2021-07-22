from wordfinder import


class SpecialWordFinder(WordFinder):
    def __init__(self, file):
        super().__init__(file)
        self.wordlist = []
        for line in self.file:
            if '#' not in line and line:
                self.wordlist.append(line.strip())
        print(f'{self.wordcount()} words read')
