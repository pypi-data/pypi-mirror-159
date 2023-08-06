from typing import Any, List
from fon.list import intersperse

def concats(xs) -> str:
    """returns a string"""
    ys = []
    for x in xs:
        ys.append(str(x))
    return ''.join(ys)


def intercalates(x, xs) -> str:
    """returns a string"""
    return concats(intersperse(x, xs))



def intersperses(x: str, s: str) -> str:
    """intersperses('.', 'hello')  ---> 'h.e.l.l.o' """
    return x.join(s)

