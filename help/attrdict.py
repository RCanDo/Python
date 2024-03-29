#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: attrdict 2.0.1
subtitle:
version: 1.0
type: package intro
keywords: [attrdict, dict]
description: |
    AttrDict is an MIT-licensed library that provides mapping objects
    that allow their elements to be accessed both as keys and as attributes:
remarks:
todo:
sources:
    - title: attrdict 2.0.1
      link: https://pypi.org/project/attrdict/
      date:    # date of issue or last edition of the page
      authors:
          - nick: MIT
    - title: Project description
      link: https://travis-ci.org/bcj/AttrDict.svg?branch=master https://coveralls.io/repos/bcj/AttrDict/badge.png?branch=master
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name:
    path: ~/ROBOCZY/Python/help/
    date: 2022-05-18
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""
#%%
from attrdict import AttrDict, AttrDefault
a = AttrDict({'foo': 'bar'})
a.foo       # 'bar'
a['foo']    # 'bar'

#%% Attribute access makes it easy to create convenient, hierarchical settings objects:

with open('settings.yaml') as fileobj:
    settings = AttrDict(yaml.safe_load(fileobj))

cursor = connect(**settings.db.credentials).cursor()

cursor.execute("SELECT column FROM table;")

#%%
"""
Installation
 AttrDict is in PyPI, so it can be installed directly using:

$ pip install attrdict

Or from Github:

$ git clone https://github.com/bcj/AttrDict
$ cd AttrDict
$ python setup.py install
"""
#%% Basic Usage
"""
AttrDict comes with three different classes, AttrMap, AttrDict, and AttrDefault.
They are all fairly similar, as they all are MutableMappings (read: dictionaries)
that allow creating, accessing, and deleting key-value pairs as attributes.

Valid Names
Any key can be used as an attribute as long as:
- The key represents a valid attribute
  (i.e., it is a string comprised only of alphanumeric characters and underscores that doesn’t start with a number)
- The key represents a public attribute (i.e., it doesn’t start with an underscore). This is done (in part) so that implementation changes between minor and micro versions don’t force major version changes.
- The key does not shadow a class attribute (e.g., get).

Attributes vs. Keys
There is a minor difference between accessing a value as an attribute
vs. accessing it as a key, is that when a dict is accessed as an attribute,
it will automatically be converted to an Attr object.
This allows you to recursively access keys:
"""
attr = AttrDict({'foo': {'bar': 'baz'}})
attr.foo.bar    # 'baz'

"""
Relatedly, by default, sequence types that aren’t bytes, str, or unicode (e.g., lists, tuples)
will automatically be converted to tuples, with any mappings converted to Attrs:
"""
attr = AttrDict({'foo': [{'bar': 'baz'}, {'bar': 'qux'}]})
for sub_attr in attr.foo:
    print(sub_attr.bar)
# 'baz'
# 'qux'

#%%
"""
To get this recursive functionality for keys that cannot be used as attributes,
you can replicate the behavior by   calling   the Attr object:
"""
attr = AttrDict({1: {'two': 3}})
attr(1).two     # 3

#%% Classes
"""
AttrDict comes with three different objects,
 AttrMap, AttrDict, and AttrDefault.
"""
#%% AttrMap
"""
The most basic implementation.
Use this if you want to limit the number of invalid keys, or otherwise cannot use AttrDict
"""
#%% AttrDict
"""
An Attr object that subclasses dict.
You should be able to use this absolutely anywhere you can use a dict.
While this is probably the class you want to use,
there are a few caveats that follow from this being a dict under the hood.

The copy method (which returns a   shallow copy   of the mapping)
returns a dict instead of an AttrDict.

Recursive attribute access results in a shallow copy,
so recursive assignment will fail (as you will be writing to a copy of that dictionary):
"""
attr = AttrDict({'foo': {}})
attr.foo.bar = 'baz'
attr.foo    # AttrDict({})

"""
Assignment as keys will still work:
"""
attr = AttrDict({'foo': {}})
attr['foo']['bar'] = 'baz'
attr.foo    # {'bar': 'baz'}
attr
"""
If either of these caveats are deal-breakers, or you don’t need your object to be a dict,
consider using AttrMap instead.
"""

#%% AttrDefault
"""
At Attr object that behaves like a defaultdict. This allows on-the-fly, automatic key creation:
"""
attr = AttrDefault(int, {})
attr.foo += 1
attr.foo    # 1
"""
AttrDefault also has a pass_key option that passes the supplied key to the default_factory:
"""
attr = AttrDefault(sorted, {}, pass_key=True)
attr.banana
['a', 'a', 'a', 'b', 'n', 'n']

#%% Merging
"""
All three Attr classes can be merged with eachother or other Mappings using the + operator.
For conflicting keys, the right dict’s value will be preferred,
but in the case of two dictionary values, they will be recursively merged:
"""
a = {'foo': 'bar', 'alpha': {'beta': 'a', 'a': 'a'}}
b = {'lorem': 'ipsum', 'alpha': {'bravo': 'b', 'a': 'b'}}

AttrDict(a) + b
# {'foo': 'bar', 'lorem': 'ipsum', 'alpha': {'beta': 'a', 'bravo': 'b', 'a': 'b'}}

#!!! NOTE: AttrDict’s add is not commutative, a + b != b + a:
a = {'foo': 'bar', 'alpha': {'beta': 'b', 'a': 0}}
b = {'lorem': 'ipsum', 'alpha': {'bravo': 'b', 'a': 1}}
b + AttrDict(a)
{'foo': 'bar', 'lorem': 'ipsum', 'alpha': {'beta': 'a', 'bravo': 'b', 'a': 0}}

#%% Sequences
"""
By default, items in non-string Sequences (e.g. lists, tuples) will be converted to AttrDicts:
"""
adict = AttrDict({'list': [{'value': 1}, {'value': 2}]})
adict
for element in adict.list:
    element.value
# 1 2
"""
This will not occur if you access the AttrDict as a dictionary:
"""
adict = AttrDict({'list': [{'value': 1}, {'value': 2}]})
for element in adict['list']:
    isinstance(element, AttrDict)
# False  False
for element in adict['list']:
    element.value
#! AttributeError: 'dict' object has no attribute 'value'

"""
To disable this behavior globally, pass the attribute recursive=False to the constructor:
"""
adict = AttrDict({'list': [{'value': 1}, {'value': 2}]}, recursive=False)
for element in adict.list:
    isinstance(element, AttrDict)
# True True
for element in adict.list:
    element.value
# 1 2
for element in adict['list']:
    element.value
#! AttributeError: 'dict' object has no attribute 'value'
#!!! hence nothing changes...
"""
When merging an AttrDict with another mapping,
this behavior will be disabled if at least one of the merged items is an AttrDict
that has set recursive to False.
"""
