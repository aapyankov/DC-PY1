# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
count = 16
list_of_numbersystems = [({"bin": bin(i), "dec": i, "hex": hex(i), "oct": oct(i)}) for i in range(count)]

pprint(list_of_numbersystems)