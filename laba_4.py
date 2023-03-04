from string import ascii_uppercase
class Alphabet:
    def __init__ (self, lang, letters):
        self.lang = lang
        self.letters = letters
    def print(self):
        print(self.letters)
    def letters_num(self):
        print(len(self.letters))
class EngAlphabet(Alphabet):
    def __init__(self, lang, letters):
        super(). __init__(lang, letters)
        self.__letters_num = len(self.letters)
    def is_en_letter(self,letter):
        return(letter in self.letters)
    def letters_num (self):
        return(self.__letters_num)
    def example(self):
        return("Don't judge a book by it's cover")
if __name__ == '__main__':
    A = EngAlphabet('En',ascii_uppercase)
    A.print()
    print(A.letters_num())
    print(A.is_en_letter('F'))
    print(A.is_en_letter('Щ'))
    print(A.example())



