#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: date & time
version: 1.0
type: tutorial
keywords: [data class]
description: |
    About data classes
remarks:
todo:
sources:
    - title: Data Classes in Python 3.7+ (Guide)
      link: https://realpython.com/python-data-classes/
      date:
      authors:
          - fullname: Geir Arne Hjelle
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name:
    path: ./Objects
    date: 2021-04-27
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%% This is block delimiter very useful for interactive work like e.g. in Spyder (part of Anaconda)

import rcando.ak as ak
import os

ROOT = "~"
#ROOT = "~"
PYWORKS = os.path.join(ROOT, "Roboczy/Python")
##
#DATA = os.path.join(ROOT, "Data/eco")           ## adjust !!!
WD = os.path.join(PYWORKS, "Objects")  ## adjust !!!

os.chdir(WD)
print(os.getcwd())

#%%
from dataclasses import dataclass

@dataclass
class DataClassCard:
    rank: str
    suit: str

#%%
queen_of_hearts = DataClassCard('Q', 'Hearts')
queen_of_hearts.rank   # 'Q'

queen_of_hearts        # DataClassCard(rank='Q', suit='Hearts')

queen_of_hearts == DataClassCard('Q', 'Hearts')  #!!! True

#%% via regular class
class RegularCard():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

queen_of_hearts = RegularCard('Q', 'Hearts')
queen_of_hearts.rank  # 'Q'

queen_of_hearts   # <__main__.RegularCard at 0x2116d3036c8>

queen_of_hearts == RegularCard('Q', 'Hearts')   #!!! False

#%% making ~ DataClass via regular class:

class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(rank={self.rank!r}, suit={self.suit!r})')

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.rank, self.suit) == (other.rank, other.suit)

# in DataClass these methods are for free

#%% Alternatives to Data Classes
#%% tuple, dictionary
queen_of_hearts_tuple = ('Q', 'Hearts')
queen_of_hearts_dict = {'rank': 'Q', 'suit': 'Hearts'}

queen_of_hearts_tuple[0]        # No named access
queen_of_hearts_dict['suit']    # Would be nicer with .suit

# no formal structure nor type;
# need to remember names and positions

#%%
from collections import namedtuple

NamedTupleCard = namedtuple('NamedTupleCard', ['rank', 'suit'])

queen_of_hearts = NamedTupleCard('Q', 'Hearts')
queen_of_hearts.rank  # 'Q'

queen_of_hearts  # NamedTupleCard(rank='Q', suit='Hearts')

queen_of_hearts == NamedTupleCard('Q', 'Hearts')  # True

# looks good but
queen_of_hearts == ('Q', 'Hearts')    # True

Person = namedtuple('Person', ['first_initial', 'last_name'])
ace_of_spades = NamedTupleCard('A', 'Spades')
ace_of_spades == Person('A', 'Spades')   #!!! True    although these are different 'types'

# moreover hard to add default value for attribute
# is immutable !
queen_of_hearts.rank = 'K'   #! AttributeError: can't set attribute


#%%
# Another alternative, and one of the inspirations for data classes,
# is the attrs project. With attrs installed (pip install attrs),
# you can write a card class as follows:
import attr

@attr.s
class AttrsCard:
    rank = attr.ib()
    suit = attr.ib()

# This can be used in exactly the same way as the DataClassCard and NamedTupleCard examples earlier.
# However, as attrs is not a part of the standard library,
# it does add an external dependency to your projects.

#%%
from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float
    lat: float

#%%
pos = Position('Oslo', 10.8, 59.9)
print(pos)
pos.lat
print(f'{pos.name} is at {pos.lat}°N, {pos.lon}°E')

#%%
from dataclasses import make_dataclass

Position = make_dataclass('Position', ['name', 'lat', 'lon'])
pos = Position('Oslo', 10.8, 59.9)
print(pos)
pos.lat
print(f'{pos.name} is at {pos.lat}°N, {pos.lon}°E')

#%%
"""
A data class is a regular Python class.
The only thing that sets it apart is that it has basic data model methods
like .__init__(), .__repr__(), and .__eq__() implemented for you.
"""

#%% default values
@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

#%%
Position('Null Island')
Position('Greenwich', lat=51.8)
Position('Vancouver', -123.1, 49.3)

#%%
"""
adding some kind of type hint is mandatory when defining the fields in your data class.
Without a type hint, the field will not be a part of the data class.
However, if you do not want to add explicit types to your data class, use
typing.Any:
"""
from dataclasses import dataclass
from typing import Any

@dataclass
class WithoutExplicitTypes:
    name: Any
    value: Any = 42

#%%
"""While you need to add type hints in some form when using data classes,
these types are NOT enforced at runtime!
The following code runs without any problems:
"""
Position(3.14, 'pi day', 2018)  # Position(name=3.14, lon='pi day', lat=2018)

#%% Adding Methods
#%%
from dataclasses import dataclass
from math import asin, cos, radians, sin, sqrt

@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

    def distance_to(self, other):
        r = 6371  # Earth radius in kilometers
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (sin((phi_2 - phi_1) / 2)**2
             + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2)**2)
        return 2 * r * asin(sqrt(h))


#%%
oslo = Position('Oslo', 10.8, 59.9)
vancouver = Position('Vancouver', -123.1, 49.3)
oslo.distance_to(vancouver)

#%%
#%%
from dataclasses import dataclass
from typing import List

@dataclass
class PlayingCard:
    rank: str
    suit: str

@dataclass
class Deck:
    cards: List[PlayingCard]

#%%
queen_of_hearts = PlayingCard('Q', 'Hearts')
ace_of_spades = PlayingCard('A', 'Spades')
two_cards = Deck([queen_of_hearts, ace_of_spades])
two_cards

#%%
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

def make_french_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]

make_french_deck()

#%%
'\N{BLACK SPADE SUIT}'
'\u2660'
#%%

@dataclass
class Deck:  # Will NOT work
    cards: List[PlayingCard] = make_french_deck()

"""
Don’t do this!
This introduces one of the most common ANTI-PATTERNS IN PYTHON:
using MUTABLE DEFAULT ARGUMENTS.
The problem is that all instances of Deck will use the same list object
as the default value of the .cards property.
This means that if, say, one card is removed from one Deck,
then it disappears from all other instances of Deck as well.
Actually, data classes try to prevent you from doing this,
and the code above will raise a ValueError.
"""
#%%
from dataclasses import dataclass, field
@dataclass
class Deck:
    cards: List[PlayingCard] = field(default_factory=make_french_deck)

"""
The argument to default_factory() can be any zero parameter callable.
Now it is easy to create a full deck of playing cards:
"""
Deck()
#%%
"""
The field() specifier is used to customize each field of a data class individually.
For reference, these are the parameters field() supports:

    default:  Default value of the field
    default_factory:  Function that returns the initial value of the field
    init:  Use field in .__init__() method? (Default is True.)
    repr:  Use field in repr of the object? (Default is True.)
    compare:  Include the field in comparisons? (Default is True.)
    hash:  Include the field when calculating hash()? (Default is to use the same as for compare.)
    metadata:  A mapping with information about the

You may not specify both `default` and `default_factory`.
"""
#%%
@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = field(default=0.0, repr=False)

Position('qq')

#%%
@dataclass
class Position:
    name: str
    lon: float = field(default=0.0, metadata={'unit': 'degrees'})
    lat: float = field(default=0.0, metadata={'unit': 'degrees'})

Position('qq')

#%%
from dataclasses import fields
fields(Position)
fields(Position)[2].metadata['unit']

#%%
#%% Representation
@dataclass
class PlayingCard:
    rank: str
    suit: str

    def __str__(self):
        return f'{self.suit}{self.rank}'

#%%
ace_of_spades = PlayingCard('A', '♠')
ace_of_spades           # PlayingCard(rank='A', suit='♠')
print(ace_of_spades)    # ♠A
print(Deck())

#%%
@dataclass
class Deck:
    cards: List[PlayingCard] = field(default_factory=make_french_deck)

    def __str__(self):
        cards = ', '.join(f'{c!s}' for c in self.cards)
        return f'{self.__class__.__name__}({cards})'

#%%
Deck()
print(Deck())  # Deck(♣2, ♣3, ♣4, ♣5, ..., ♠10, ♠J, ♠Q, ♠K, ♠A)

#%%
for c in make_french_deck(): print(f"{c!s}", end=" ")
# {c!s}  means use string represantation for `c`

#%%
#%% Comparisons
queen_of_hearts = PlayingCard('Q', '♡')
ace_of_spades = PlayingCard('A', '♠')
ace_of_spades > queen_of_hearts   #! TypeError: '>' not supported between

#%%
@dataclass(order=True)
class PlayingCard:
    rank: str
    suit: str

    def __str__(self):
        return f'{self.suit}{self.rank}'

#%%
"""
you can also give parameters to the @dataclass() decorator in parentheses.
The following parameters are supported:

    init:  Add .__init__() method? (Default is True.)
    repr:  Add .__repr__() method? (Default is True.)
    eq:  Add .__eq__() method? (Default is True.)
    order:  Add ordering methods? (Default is False.)
    unsafe_hash:  Force the addition of a .__hash__() method? (Default is False.)
    frozen:  If True, assigning to fields raise an exception. (Default is False.)

"""
#%%
queen_of_hearts = PlayingCard('Q', '♡')
ace_of_spades = PlayingCard('A', '♠')
ace_of_spades > queen_of_hearts     # False  -- because A < Q by default

sorted([ace_of_spades, queen_of_hearts])
sorted([queen_of_hearts, ace_of_spades])

#%%
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()
card = PlayingCard('Q', '♡')
RANKS.index(card.rank) * len(SUITS) + SUITS.index(card.suit)   # 42
    #??? WHAT RANKING SYSTEM IS IT ???

#%%
from dataclasses import dataclass, field

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

@dataclass(order=True)
class PlayingCard:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS)
                           + SUITS.index(self.suit))

    def __str__(self):
        return f'{self.suit}{self.rank}'

"""
Note that .sort_index is added as the first field of the class.
That way, the comparison is first done using .sort_index and only
if there are ties are the other fields used.
Using field(), you must also specify that .sort_index should not be included
as a parameter in the .__init__() method
(because it is calculated from the .rank and .suit fields).
To avoid confusing the user about this implementation detail,
it is probably also a good idea to remove .sort_index from the repr of the class.
"""
#%%
queen_of_hearts = PlayingCard('Q', '♡')
ace_of_spades = PlayingCard('A', '♠')
ace_of_spades > queen_of_hearts

print(Deck(sorted(make_french_deck())))

#%%
from random import sample
deck = Deck(sample(make_french_deck(), k=10))
print(deck)

#%%
#%% Immutable Data Classes
@dataclass(frozen=True)
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

#%%
pos = Position('Oslo', 10.8, 59.9)
pos.name

pos.name = 'Stockholm'   #! FrozenInstanceError: cannot assign to field 'name'

#%%
"""
Be aware though that if your data class contains mutable fields,
those might still change.
This is true for all nested data structures in Python:
"""
from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class ImmutableCard:
    rank: str
    suit: str

    def __repr__(self):
        return f'{self.suit}{self.rank}'


@dataclass(frozen=True)
class ImmutableDeck:
    cards: List[ImmutableCard]

    def __repr__(self):
        res = ""
        for card in self.cards:
            res += f'{card.suit}{card.rank} '
        return res
"""
Even though both ImmutableCard and ImmutableDeck are immutable,
the list holding cards is not.
You can therefore still change the cards in the deck:
"""
#%% !!!
queen_of_hearts = ImmutableCard('Q', '♡')
ace_of_spades = ImmutableCard('A', '♠')
deck = ImmutableDeck([queen_of_hearts, ace_of_spades])
deck  # ♡Q ♠A

deck.cards[0] = ImmutableCard('7', '♢')
deck  # ♢7 ♠A
#!!!

deck.cards.append(ImmutableCard('K', '♣'))
deck

#%%
#%% Inheritance

@dataclass
class Position:
    name: str
    lon: float
    lat: float

@dataclass
class Capital(Position):
    country: str

Capital('Oslo', 10.8, 59.9, 'Norway')
# Capital(name='Oslo', lon=10.8, lat=59.9, country='Norway')

#%%
"""
The country field of Capital is added after the three original fields in Position.
Things get a little more complicated if any fields in the base class
have default values:
"""
@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

@dataclass
class Capital(Position):
    country: str
    #! TypeError: non-default argument 'country' follows default argument

#%%
@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

@dataclass
class Capital(Position):
    country: str = None
    lat: float = 40.0

Capital('Madrid', country='Spain')
# Capital(name='Madrid', lon=0.0, lat=40.0, country='Spain')

#%%
#%% Optimizing Data Classes

@dataclass
class SimplePosition:
    name: str
    lon: float
    lat: float

@dataclass
class SlotPosition:
    __slots__ = ['name', 'lon', 'lat']
    name: str
    lon: float
    lat: float

#%%
from pympler import asizeof
simple = SimplePosition('London', -0.1, 51.5)
slot = SlotPosition('Madrid', -3.7, 40.4)
asizeof.asizesof(simple, slot)

#%%
from timeit import timeit
timeit('slot.name', setup="slot=SlotPosition('Oslo', 10.8, 59.9)", globals=globals())
# 0.13451020000502467
timeit('simple.name', setup="simple=SimplePosition('Oslo', 10.8, 59.9)", globals=globals())
# 0.13348109999787994

# no difference...

#%%
