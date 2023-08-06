
from itertools import chain, repeat
from typing import Any, List


def concat(lists) -> List[Any]:
    """returns a list of merging the original list of lists"""
    return list(chain.from_iterable(lists))


def drop(drop: int, xs) -> Any:
    """works on lists, strings, ranges, it returns the original type"""
    return xs[drop:]


def dropl(drop: int, xs) -> List[Any]:
    """always returns a list"""
    return list(xs[drop:])

def drop_take(drop: int, take: int, xs) -> Any:
    """works on lists and strings"""
    return xs[drop:drop+take]


def drop_takel(drop: int, take: int, xs) -> List[Any]:
    """always returns a list"""
    return list(xs[drop:drop+take])


def intercalate(xs, xss) -> str:
    """returns a combined list"""
    return concat(intersperse(xs, xss))



def intersperse(a, xs) -> List[Any]:
    """examples:
    intersperse(0, [1,2,3]  ---> [1,0,2,0,3] """
    ys = []
    for x in xs:
        ys.append(x)
        ys.append(a)
    return ys[:-1]



def replicate(i: int, x) -> List[Any]:
    """works on any types of data, always return a list"""
    return list(repeat(x, i))





def reverse(x) -> Any:
    """can reverse lists, ranges and strings, return the original type"""
    return x[::-1]


def reversel(x) -> List[Any]:
    """reversel() always return a list, if this function is used in strings, it will return a list of characters / list of single string"""
    return list(x[::-1])

def take(take: int, xs) -> Any:
    """works on lists and strings"""
    return xs[:take]


def takel(take: int, xs) -> List[Any]:
    """always returns a list"""
    return list(xs[:take])