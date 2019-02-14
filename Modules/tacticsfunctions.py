import sys
from enum import Enum, auto

def move(person, location):
    person.location[0] = location[0]
    person.location[1] = location[1]

class Actions(Enum):
    MOVE = auto()
    SELECT = auto()

def end():
    sys.exit()
