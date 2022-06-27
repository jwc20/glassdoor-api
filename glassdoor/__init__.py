from .core import *
from .class_a import ClassA
from .class_b import ClassB


class BS4Scraper(ClassA, ClassB):
    def __init__(self, keywords=[], *args):
        ClassA.__init__(self, keywords=keywords, *args)
        ClassB.__init__(self, keywords=keywords, *args)


__authors__ = [""]
__source__ = "https://github.com/jwc20/bs4-scraper-boilerplate"
__license__ = "MIT"

__all__ = [""]
