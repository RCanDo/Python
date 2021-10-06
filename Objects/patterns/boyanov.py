#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Python Design Patterns
subtitle:
version: 1.0
type: tutorial
keywords: [design pattern, objects, behavioral]
description: |
    About behavioral design patterns.
remarks:
    - etc.
todo:
    - problem 1
sources:
    - title: Python Design Patterns
      link: https://www.toptal.com/python/python-design-patterns
      date:
      authors:
          - fullname: Andrei Boyanov
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name:
    path: .../Python/datetime
    date: 2021-04-27
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%% This is block delimiter very useful for interactive work like e.g. in Spyder (part of Anaconda)

#%%
from rcando.ak.builtin import * #flatten, paste
from rcando.ak.nppd import * #data_frame
import os, sys, json

ROOT = json.load(open('root.json'))
WD = os.path.join(ROOT['Works'], "Python/Objects/")   #!!! adjust
os.chdir(WD)

print(os.getcwd())

#%%
"""

1. Program to an interface not an implementation.
    Easier to ask for forgivness then for permission (EAFP)
    == duck typing == `try ... except ...`
   instead of
    Look before you leep (LBYL)
    == `if ... else ...`

2. Favor object composition over inheritance.

Patterns are not invented, they are discovered.
They exist, we just need to find and put them to use.

Behavioural Patterns involve communication between objects, how objects interact and fulfil a given task.
According to GOF principles, there are a total of 11 behavioral patterns in Python:
    Iterator,
    Chain of responsibility,
    Command,
    Interpreter,
    Mediator,
    Memento,
    Observer,
    State,
    Strategy,
    Template,
    Visitor.
"""
#%% Iterator - built-in

#%% Chain of responsibility
"""
Every piece of code must do one, and only one, thing.

For example, if we want to filter some content we can implement different filters,
each one doing one precise and clearly defined type of filtering.
These filters could be used to filter offensive words, ads, unsuitable video content, and so on.
"""

class ContentFilter(object):

    def __init__(self, filters=None):
        self._filters = list()
        if filters is not None:
            self._filters += filters

    def filter(self, content):
        for filter in self._filters:
            content = filter(content)
        return content

filter = ContentFilter([
                offensive_filter,
                ads_filter,
                porno_video_filter])

filtered_content = filter.filter(content)

#%% Command
"""
The command pattern is handy in situations when, for some reason,
we need to start by preparing what will be executed and then to execute it when needed.

The advantage is that encapsulating actions in such a way enables Python developers
to add additional functionalities related to the executed actions,
such as undo/redo, or keeping a history of actions and the like.

Let’s see what a simple and frequently used example looks like:
"""
class RenameFileCommand(object):
    def __init__(self, from_name, to_name):
        self._from = from_name
        self._to = to_name

    def execute(self):
        os.rename(self._from, self._to)

    def undo(self):
        os.rename(self._to, self._from)

class History(object):
    def __init__(self):
        self._commands = list()

    def execute(self, command):
        self._commands.append(command)
        command.execute()

    def undo(self):
        self._commands.pop().undo()

history = History()
history.execute(RenameFileCommand('docs/cv.doc', 'docs/cv-en.doc'))
history.execute(RenameFileCommand('docs/cv1.doc', 'docs/cv-bg.doc'))
history.undo()
history.undo()

#%%
#%% Creational Patterns
"""
Let’s start by pointing out that creational patterns are not commonly used in Python.
Why? Because of the dynamic nature of the language.

Someone wiser than I once said that __Factory__ is built into Python.
It means that the language itself provides us with all the flexibility we need
to create objects in a sufficiently elegant fashion;
we rarely need to implement anything on top, like __Singleton__ or __Factory__.

In one Python Design Patterns tutorial, I found a description of the creational design patterns
that stated these design
“patterns provide a way to create objects while hiding the creation logic,
 rather than instantiating objects directly using a `new` operator.”

That pretty much sums up the problem: We don’t have a `new` operator in Python!

Nevertheless, let’s see how we can implement a few,
should we feel we might gain an advantage by using such patterns.
"""

#%% Singleton
"""
The Singleton pattern is used when we want to guarantee
that only one instance of a given class exists during runtime.
Do we really need this pattern in Python?

Based on my experience, it’s easier to simply create one instance intentionally
and then use it instead of implementing the Singleton pattern.

But should you want to implement it, here is some good news:
In Python, we can alter the instantiation process (along with virtually anything else).
Remember the __new__() method I mentioned earlier?
Here we go:
"""
class Logger(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_logger'):
            cls._logger = super(Logger, cls).__new__(cls, *args, **kwargs)
        return cls._logger

"""
In this example, Logger is a Singleton.

These are the alternatives to using a Singleton in Python:

    Use a module.

    Create one instance somewhere at the top-level of your application, perhaps in the config file.

    Pass the instance to every object that needs it.
    That’s a dependency injection and it’s a powerful and easily mastered mechanism.


see:
    ../../ExpertPython/14-DesignPatterns/01-singleton.py
    ../on_new_and_init.py
"""


#%% Dependency Injection (DI) / Inversion of Control (IoC)
#
"""
Do NOT mess it up with Dependency Inversion (last of SOLID principles)
although there is connection between them.
---

I don’t intend to get into a discussion on whether dependency injection is a design pattern,
but I will say that it’s a very good mechanism of implementing __loose couplings__,
and it helps make our application maintainable and extendable.
Combine it with Duck Typing and the Force will be with you. Always.

I listed it in the creational pattern section of this post because it deals with the question
of when (or even better: where) the object is created.
It’s created outside.

Better to say that the objects are not created at all where we use them,
so the dependency is not created where it is consumed.
The consumer code receives the externally created object and uses it.
For further reference, please read the most upvoted answer to this Stackoverflow question.

It’s a nice explanation of dependency injection and gives us a good idea
of the potential of this particular technique.
Basically the answer explains the problem with the following example:
Don’t get things to drink from the fridge yourself, state a need instead.
Tell your parents that you need something to drink with lunch.

Python offers us all we need to implement that easily.
Think about its possible implementation in other languages such as Java and C#,
and you’ll quickly realize the beauty of Python.

Let’s think about a simple example of dependency injection:
"""
class Command:

    def __init__(self, authenticate=None, authorize=None):
        self.authenticate = authenticate or self._not_authenticated
        self.authorize = authorize or self._not_autorized

    def execute(self, user, action):
        self.authenticate(user)
        self.authorize(user, action)
        return action()

if in_sudo_mode:
    command = Command(always_authenticated, always_authorized)
else:
    command = Command(config.authenticate, config.authorize)

command.execute(current_user, delete_user_action)

"""
We inject the authenticator and authorizer methods in the Command class.
All the Command class needs is to execute them successfully
without bothering with the implementation details.
This way, we may use the Command class with
whatever authentication and authorization mechanisms we decide to use in runtime.

We have shown how to inject dependencies through the constructor,
but we can easily inject them by setting directly the object properties,
unlocking even more potential:
"""
command = Command()

if in_sudo_mode:
    command.authenticate = always_authenticated
    command.authorize = always_authorized
else:
    command.authenticate = config.authenticate
    command.authorize = config.authorize

command.execute(current_user, delete_user_action)

"""
There is much more to learn about dependency injection;
curious people would search for IoC (Inversion of Control), for example.

But before you do that, read another Stackoverflow answer, the most upvoted one to this question.

Again, we just demonstrated how implementing this wonderful design pattern
in Python is just a matter of using the built-in functionalities of the language.

Let’s not forget what all this means:
The dependency injection technique allows for very flexible and easy unit-testing.
Imagine an architecture where you can change data storing on-the-fly.
Mocking a database becomes a trivial task, doesn’t it?
For further information, you can check out Toptal’s Introduction to Mocking in Python.
https://www.toptal.com/python/an-introduction-to-mocking-in-python

You may also want to research
    Prototype,
    Builder and
    Factory
design patterns.
"""


#%%
#%% Structural Patterns

#%% Facade
"""
This may very well be the most famous Python design pattern.

Imagine you have a system with a considerable number of objects.
Every object is offering a rich set of API methods.
You can do a lot of things with this system, but how about simplifying the interface?

Why not add an interface object exposing a well thought-out subset of all API methods?
A Facade!
"""

class Car(object):

    def __init__(self):
        self._tyres = [Tyre('front_left'),
                       Tyre('front_right'),
                       Tyre('rear_left'),
                       Tyre('rear_right'), ]
        self._tank = Tank(70)

    def tyres_pressure(self):
        return [tyre.pressure for tyre in self._tyres]

    def fuel_level(self):
        return self._tank.level

#%% Adapter
"""
If Facades are used for interface simplification, Adapters are all about altering the interface.
Like using a cow when the system is expecting a duck.

Let’s say you have a working method for logging information to a given destination.
Your method expects the destination to have a write() method (as every file object has, for example).
"""
def log(message, destination):
    destination.write('[{}] - {}'.format(datetime.now(), message))

"""
I would say it is a well written method with dependency injection,
which allows for great extensibility.
Say you want to log to some UDP socket instead to a file,
you know how to open this UDP socket but the only problem is that the socket object has no write() method.
You need an Adapter!
"""

import socket

class SocketWriter(object):

    def __init__(self, ip, port):
        self._socket = socket.socket(socket.AF_INET,
                                     socket.SOCK_DGRAM)
        self._ip = ip
        self._port = port

    def write(self, message):
        self._socket.send(message, (self._ip, self._port))

def log(message, destination):
    destination.write('[{}] - {}'.format(datetime.now(), message))

upd_logger = SocketWriter('1.2.3.4', '9999')
log('Something happened', udp_destination)

"""
But why do I find adapter so important?
Well, when it’s effectively combined with dependency injection, it gives us huge flexibility.
Why alter our well-tested code to support new interfaces
when we can just implement an adapter that will translate the new interface
to the well known one?

You should also check out and master
    Bridge  and  Proxy  design patterns,
due to their similarity to adapter.
Think how easy they are to implement in Python,
and think about different ways you could use them in your project.
"""

#%% Decorator
# see ../decorators/*


#%%


#%%