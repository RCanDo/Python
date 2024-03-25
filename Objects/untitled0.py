#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 10:50:08 2023

@author: arek

https://realpython.com/python-super/#an-overview-of-pythons-super-function
"""

# %%
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)


# %%
class Cube(Square):
    def surface_area(self):
        face_area = super(Square, self).area()
        return face_area * 6

    def volume(self):
        face_area = super(Square, self).area()
        return face_area * self.length


# %%

cube = Cube(3)
cube
dir(cube)
cube.length
cube.width
cube.area()
cube.volume()

# %% multiple ingeritance

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area


# %%
pyramid = RightPyramid(2, 4)
pyramid.area()

RightPyramid.__mro__


# %%
class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(self.base)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

# %%
RightPyramid.__mro__
pyramid = RightPyramid(2, 4)
pyramid.area()

# %%
class Rectangle:
    def __init__(self, length, width, **kwargs):
        print("start Rectangle init")
        self.length = length
        self.width = width
        super().__init__(**kwargs)
        print("end Rectangle init")

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from
# the Rectangle class
class Square(Rectangle):
    def __init__(self, length, **kwargs):
        print("start Square init")
        super().__init__(length=length, width=length, **kwargs)
        print("end Square init")

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

class Triangle:
    def __init__(self, base, height, **kwargs):
        print("start Triangle init")
        self.base = base
        self.height = height
        super().__init__(**kwargs)
        print("end Triangle init")

    def tri_area(self):
        return 0.5 * self.base * self.height

class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        print("start RightPyramid init")
        self.base = base
        self.slant_height = slant_height
        kwargs["height"] = slant_height
        kwargs["length"] = base
        super().__init__(base=base, **kwargs)
        print("end RightPyramid init")

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area


rp = RightPyramid(3, 4)
rp.area_2()

# %%

class First(object):
    def __init__(self):
        super(First, self).__init__()
        print("first")

class Second(object):
    def __init__(self):
        super(Second, self).__init__()
        print("second")

class Third(First, Second):
    def __init__(self):
        super(Third, self).__init__()
        print("third")

Third.__mro__
Third()

# %%  !!!
# %%  https://www.datacamp.com/tutorial/super-multiple-inheritance-diamond-problem

class Tokenizer:
    """Tokenize text"""
    def __init__(self, text):
        print('Start Tokenizer.__init__()')
        self.tokens = text.split()
        print('End Tokenizer.__init__()')


class WordCounter(Tokenizer):
    """Count words in text"""
    def __init__(self, text):
        print('Start WordCounter.__init__()')
        super().__init__(text)
        self.word_count = len(self.tokens)
        print('End WordCounter.__init__()')


class Vocabulary(Tokenizer):
    """Find unique words in text"""
    def __init__(self, text):
        print('Start init Vocabulary.__init__()')
        super().__init__(text)
        self.vocab = set(self.tokens)
        print('End init Vocabulary.__init__()')


class TextDescriber(WordCounter, Vocabulary):
    """Describe text with multiple metrics"""
    def __init__(self, text):
        print('Start init TextDescriber.__init__()')
        super().__init__(text)
        print('End init TextDescriber.__init__()')


td = TextDescriber('row row row your boat')
print('--------')
print(td.tokens)
print(td.vocab)
print(td.word_count)

TextDescriber.__mro__

# %%
"""
Start init TextDescriber.__init__()
Start WordCounter.__init__()
Start init Vocabulary.__init__()
Start Tokenizer.__init__()
End Tokenizer.__init__()
End init Vocabulary.__init__()
End WordCounter.__init__()
End init TextDescriber.__init__()
--------
['row', 'row', 'row', 'your', 'boat']
{'boat', 'row', 'your'}
5

(__main__.TextDescriber,
 __main__.WordCounter,
 __main__.Vocabulary,
 __main__.Tokenizer,
 object)
"""

# %%%  no diamond
class TokenizerA:
    """Tokenize text"""
    def __init__(self, text):
        print('Start TokenizerA.__init__()')
        self.tokens = text.split()
        print('End TokenizerA.__init__()')

class TokenizerB:
    """Tokenize text"""
    def __init__(self, text):
        print('Start TokenizerB.__init__()')
        self.tokens = text.split()
        print('End TokenizerB.__init__()')

class WordCounter2(TokenizerA):
    """Count words in text"""
    def __init__(self, text):
        print('Start WordCounter.__init__()')
        super().__init__(text)
        self.word_count = len(self.tokens)
        print('End WordCounter.__init__()')


class Vocabulary2(TokenizerB):
    """Find unique words in text"""
    def __init__(self, text):
        print('Start init Vocabulary.__init__()')
        super().__init__(text)
        self.vocab = text.split()
        print('End init Vocabulary.__init__()')


class TextDescriber2(WordCounter2, Vocabulary2):
    """Describe text with multiple metrics"""
    def __init__(self, text):
        print('Start init TextDescriber.__init__()')
        super().__init__(text)
        print('End init TextDescriber.__init__()')


td2 = TextDescriber2('row row row your boat')
print('--------')
print(td2.tokens)
print(td2.vocab)
print(td2.word_count)

TextDescriber2.__mro__


# %%