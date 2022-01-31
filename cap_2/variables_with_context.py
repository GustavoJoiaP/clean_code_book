# The first thing I write a long function
def printGuessStatistics(candidate: str, count: int):
    number: str
    verb: str
    pluralModifier: str

    if count == 0:
        number = "no"
        verb = "are"
        pluralModifier = "s"
    elif count == 1:
        number = "1"
        verb = "is"
        pluralModifier = ""
    else:
        number = str(count)
        verb = "are"
        pluralModifier = "s"

    print("There" + verb + number + candidate + pluralModifier)


# The other form to resolve and simplify the long function is:
# Create a class with short methods
class GuessStaticsMessage:
    number: str
    verb: str
    pluralModifier: str

    def __init__(self, number: str, verb: str, pluralModifier: str):
        self.number = number
        self.verb = verb
        self.pluralModifier = pluralModifier

    # Method to make variables and return the message
    def make(self, candidate: str, count: int):
        self.createPluralDependentMessageParts(count)
        print('There' + self.verb + self.number + candidate + self.pluralModifier)

    # Method to validate the variable and return the variables to method make
    def createPluralDependentMessageParts(self, count: int):
        if count == 0:
            self.thereAreNoLetters()
        elif count == 1:
            self.thereIsOneLetter(count)
        else:
            self.thereAreManyLetters(count)

    # Method to return the variables value with no letters
    def thereAreNoLetters(self):
        self.number = 'no'
        self.verb = 'are'
        self.pluralModifier = 's'

    # Method to return the variables value with one letters
    def thereIsOneLetter(self, count: int):
        self.number = '1'
        self.verb = 'is'
        self.pluralModifier = ''

    # Method to return the variables value with two or more letters.
    def thereAreManyLatters(self, count: int):
        self.number = str(count)
        self.verb = 'are'
        self.pluralModifier = 's'
