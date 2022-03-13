from dataclasses import dataclass, field, fields
from typing import Any, List, Dict, Set
from copy import deepcopy


@dataclass
class Sub:
    p: Any = None
    q: Any = None

    def __repr__(self):
        ind = " "*4
        res = "\n" + "\n".join(ind + f"{k} : {v}" for k, v in self.__dict__.items())
        return res

    def to_dict(self):
        def to_dict(x):
            try:
                return x.to_dict()
            except:
                return x
        dic = {k: to_dict(v) for k, v in self.__dict__.items()}
        return dic

@dataclass
class Main:
    a: Any = field(default_factory = lambda: Sub(None, None))   #!!!  if not  default_factory(...)  then !!!
                                                               # Sub()  are mutables and behaves almost like singletons !
                                                               # each new Main() has the same values !!!
                                                               # unless you call them with explicit values of params.
    b: Any = field(default_factory = lambda: Sub(None, None))

    def __post_init__(self):
        self = deepcopy(self)

    def __repr__(self):
        ind = " "*3
        res = "\n" + "\n".join(ind + f"{k} : {v!r}" for k, v in self.__dict__.items())
        return res

    def to_dict(self):
        def to_dict(x):
            try:
                return x.to_dict()
            except:
                return x
        dic = {k: to_dict(v) for k, v in self.__dict__.items()}
        return dic

#%%

m1 = Main()
m1
m1.a.p=1
m1

m2 = Main()
m2

m3=Main(Sub(None, None), Sub(None, None))
m3

m3.b.q=4
m1
m2
m3

m4=Main()
m4
m4.a.q=2
m1
m2
m3
m4

m1==m2
m1 is m2   # False

#%%
