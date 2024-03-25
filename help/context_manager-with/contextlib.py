#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Python Module Of The Week
subtitle: contextlib
version: 1.0
type: tutorial
keywords: [context manager, contextlib]
description: |
    About built-in context manager and `contextlib` library
remarks:
    - etc.
todo:
    - problem 1
sources:
    - title: Contextlib
      link: https://pymotw.com/3/contextlib/index.html
    - link: https://docs.python.org/3.7/library/contextlib.html
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    date: 2021-09-20
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%%
import utils.ak as ak
import utils.builtin as bi
import os, sys, json

from contextlib import ContextDecorator, contextmanager

#%%
with open('pymotw.txt', 'wt') as f:
    f.write('contents go here')
# file is automatically closed
# (but not removed! for real temporary file use  tempfile  lib)

os.listdir(".")

#%%
"""
A context manager is enabled by the `with` statement, and the API involves two methods.

The `__enter__()` method is run when execution flow enters the code block inside the `with`.
It returns an object to be used within the context.

When execution flow leaves the `with` block,
the `__exit__()` method of the context manager is called to clean up any resources being used.

Combining a context manager and the `with` statement is a more compact way
of writing a `try:finally block`,
since the context manager’s `__exit__()` method is always called, even if an exception is raised.
"""
class Context:

    def __init__(self):
        print('__init__()')

    def __enter__(self):
        print('__enter__()')
        return self                  #!!!

    def __exit__(self, exc_type, exc_val, exc_tb):      # type, value, traceback
        print('__exit__()')


with Context():
    print('Doing work in the context')

"""
__init__()
__enter__()
Doing work in the context
__exit__()
"""
#%%
with Context() as c:
    print(c)
    print(c.__dict__)
    print(vars(c))

"""
__init__()
__enter__()
<__main__.Context object at 0x000001F16812FFA0>
{}
{}
__exit__()
"""

#%%
"""
The `__enter__()` method can return any object to be associated with a name
specified in the `as` clause of the `with` statement.
In this example, the Context returns an object that uses the open context.
"""

class WithinContext:

    def __init__(self, context):
        print('WithinContext.__init__({})'.format(context))

    def do_something(self):
        print('WithinContext.do_something()')

    def __del__(self):
        print('WithinContext.__del__')


class Context:

    def __init__(self):
        print('Context.__init__()')

    def __enter__(self):
        print('Context.__enter__()')
        return WithinContext(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Context.__exit__()')


with Context() as c:
    c.do_something()

#%%
"""
Context.__init__()
Context.__enter__()
WithinContext.__init__(<__main__.Context object at 0x7f90844b56f0>)
WithinContext.__del__               # ??? why here ???
WithinContext.do_something()
Context.__exit__()

The value associated with the variable `c` is the object returned by `__enter__()`,
which is not necessarily the Context instance created in the `with` statement.        !!!
i.e. as in the top example where __enter__ returns `self`.
"""
#%%  __exit__()
"""
The __exit__() method receives arguments containing details of any exception raised in the `with` block.
"""
class Context:

    def __init__(self, handle_error: bool):
        print('__init__({})'.format(handle_error))
        self.handle_error = handle_error        # True/False

    def __enter__(self):
        print('__enter__()')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__()')
        print('  exc_type =', exc_type)
        print('  exc_val  =', exc_val)
        print('  exc_tb   =', exc_tb)
        return self.handle_error                # !!!


# %%
with Context(True):
    raise RuntimeError('error message handled')
    # if `handle_error = True` error is handled (supressed and no info)
print('qq')     # is printed

# %%
with Context(False):
    raise RuntimeError('error message propagated')
    # if `handle_error = False` error is propagated (breaks execution and info displayed)
print('qq')     # not printed as error was propagated (not supressed) -- execution of the whole program broken

#%%
"""
!!!
If the context manager is meant  to handle the exception,
    __exit__() must return a `True` value
what indicates that the exception does not need to be propagated.
!!!

Returning `False` causes the exception to be re-raised after __exit__() returns,
i.e. exception is propagated.

__init__(True)
__enter__()
__exit__()
  exc_type = <class 'RuntimeError'>
  exc_val  = error message handled
  exc_tb   = <traceback object at 0x101c94948>

__init__(False)
__enter__()
__exit__()
  exc_type = <class 'RuntimeError'>
  exc_val  = error message propagated
  exc_tb   = <traceback object at 0x101c94948>
Traceback (most recent call last):
  File "contextlib_api_error.py", line 34, in <module>
    raise RuntimeError('error message propagated')

RuntimeError: error message propagated
"""

#%%
#%% Context Managers as Function Decorators

#%%
"""
The class ContextDecorator adds support to regular context manager classes
to let them be used as _function decorators_ as well as _context managers_.
"""
from contextlib import ContextDecorator

class Context(ContextDecorator):

    def __init__(self, how_used):
        self.how_used = how_used
        self.value = 1
        print('Context.__init__({})'.format(how_used))

    def __enter__(self):
        print('Context.__enter__({})'.format(self.how_used))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Context.__exit__({})'.format(self.how_used))

with Context('as context manager') as c:
    print('Doing work in the context')
    print(c.value)

# %%
"""
Context.__init__(as context manager)
Context.__enter__(as context manager)
Doing work in the context
1
Context.__exit__(as context manager)
"""

#%%
@Context('as decorator')
def func(message):
    print(message)
 # Context.__init__(as decorator)

func('Doing work in the wrapped function')
 # Context.__init__() executes at definition !

# %%
"""
Context.__enter__(as decorator)
Doing work in the wrapped function
Context.__exit__(as decorator)
"""

#%%
"""
!!!
One difference with using the context manager as a decorator is that
    the value returned by __enter__()
    is not available
    inside the function being decorated,
unlike when using `with` and `as`.
!!!

??? Hence what's the point of such context ??? (ak)
! Give some sensible useful example !

Arguments passed to the decorated function are available in the usual way.
"""

#%%
#%%  From Generator to Context Manager
"""
Creating context managers the traditional way,
by writing a class with __enter__() and __exit__() methods, is not difficult.

But sometimes writing everything out fully is extra overhead for a trivial bit of context.
In those sorts of situations, use the contextmanager() decorator to convert a generator function
into a context manager.

The context manager returned by contextmanager() is derived from ContextDecorator,
so it also works as a function decorator.
"""
from contextlib import contextmanager

@contextmanager
def make_context(arg):
    try:                # __enter__(self):
        print('  entering')
        print("  ...do sth on entering the context...")
        # ...           #     ...
        yield {arg,}    #     return {arg,}   # not accesible when `make_context()` used as decorator
    except RuntimeError as err:
        print('  ERROR:', err)
    finally:            # __exit__(self, ...)
        print('  exiting')

#%% with ... as ...

print('Normal:')
with make_context(1) as value:
    print('  inside with statement:', value)

print('Handled error:')
with make_context(1) as value:
    raise RuntimeError('showing example of handling an error')
    print('  inside with statement:', value)

print('Unhandled error:')
with make_context(1) as value:
    raise ValueError('this exception is not handled')
    print('  inside with statement:', value)

#%%
"""
The generator should
    initialize the context,
    yield exactly one time,
    then clean up the context.
The value yielded, if any, is bound to the variable in the `as` clause of the `with` statement.

Exceptions from within the `with` block are re-raised inside the generator, so they can be handled there.

Normal:
  entering
  ...do sth on entering the context...
  inside with statement: {1}
  exiting

Handled error:
  entering
  ...do sth on entering the context...
  ERROR: showing example of handling an error
  exiting

Unhandled error:
  entering
  ...do sth on entering the context...
  exiting
Traceback (most recent call last):
  File "contextlib_contextmanager.py", line 33, in <module>
    raise ValueError('this exception is not handled')
ValueError: this exception is not handled
"""
#%%  as decorator

@make_context(1)
def normal():
    print('  inside with statement')

print('Normal:')
normal()
# notice that `value` = {1} is not returned

@make_context(1)
def throw_error(err):
    raise err

print('Handled error:')
throw_error(RuntimeError('showing example of handling an error'))

print('Unhandled error:')
throw_error(ValueError('this exception is not handled'))

#%%
"""
As in the ContextDecorator example above,
when the context manager is used as a decorator the value yielded by the generator is not available
inside the function being decorated.
Arguments passed to the decorated function are still available,
as demonstrated by throw_error() in this example.

Normal:
  entering
  ...do sth on entering the context...
  inside with statement
  exiting

Handled error:
  entering
  ...do sth on entering the context...
  ERROR: showing example of handling an error
  exiting

Unhandled error:
  entering
  ...do sth on entering the context...
  exiting
Traceback (most recent call last):
  File "contextlib_contextmanager_decorator.py", line 43, in <module>
    throw_error(ValueError('this exception is not handled'))
  File ".../lib/python3.7/contextlib.py", line 74, in inner
    return func(*args, **kwds)
  File "contextlib_contextmanager_decorator.py", line 33, in throw_error
    raise err
ValueError: this exception is not handled
"""

#%%
#%%  Closing Open Handles
"""
The file class supports the context manager API directly,
but some other objects that represent open handles do not.
The example given in the standard library documentation for contextlib is the object returned from urllib.urlopen().
There are other legacy classes that use a close() method but do not support the context manager API.
To ensure that a handle is closed, use closing() to create a context manager for it.
"""
from contextlib import closing

class Door:

    def __init__(self):
        print('  __init__()')
        self.status = 'open'

    def close(self):               #!!!
        print('  close()')
        self.status = 'closed'

#%%
print('Normal Example:')

with closing(Door()) as door:
    print('  inside with statement: {}'.format(door.status))

print('  outside with statement: {}'.format(door.status))

print('  outside with statement: {}'.format(Door().status))

print('Error handling example:')
try:
    with closing(Door()) as door:
        print('  raising from inside with statement')
        raise RuntimeError('error message')
except Exception as err:
    print('  Had an error:', err)

#%%
"""
The handle is closed whether there is an error in the `with` block or not.

Normal Example:
  __init__()
  inside with statement: open
  close()
  outside with statement: closed

Error handling example:
  __init__()
  raising from inside with statement
  close()
  Had an error: error message

Hence it works like __enter__(...) of contextmanager returns False -- no error suppressing :(
help(closing)

? What's the point of using it ?
Very little "simplification" while less explicit code. Nonsense!
"""

# %%
with closing(Door()) as door:
    print('  raising from inside with statement')
    raise RuntimeError('error message')
print('sth after')      # not printed as non suppresed error occured within `with` statement.


#%%
#%%  Ignoring Exceptions
"""
It is frequently useful to ignore exceptions raised by libraries,
because the error indicates that the desired state has already been achieved,
or it can otherwise be ignored.

The most common way to ignore exceptions is with a try:except statement
with only a pass statement in the except block.
"""

class NonFatalError(Exception):
    pass

def non_idempotent_operation():
    raise NonFatalError('The operation failed because of existing state')

try:
    print('trying non-idempotent operation')
    non_idempotent_operation()
    print('succeeded!')
except NonFatalError:
    pass                    #!!!

print('continue: NonFatalError ignored')

# In this case, the operation fails but the error is ignored.

#%%
"""
The try:except form can be replaced with contextlib.suppress()
to more explicitly suppress a class of exceptions happening anywhere in the with block.
"""
from contextlib import suppress

with suppress(NonFatalError):
    print('trying non-idempotent operation')
    non_idempotent_operation()
    print('succeeded!')         # not printed

print('continue: NonFatalError ignored')    # printed but only if NonFatalError occures (or no error)

# %%
#%% Redirecting Output Streams
"""
Poorly designed library code may write directly to sys.stdout or sys.stderr,
without providing arguments to configure different output destinations.

The redirect_stdout() and redirect_stderr() context managers can be used
to capture output from functions like this,
for which the source cannot be changed to accept a new output argument.
"""
from contextlib import redirect_stdout, redirect_stderr
import io
import sys

def misbehaving_function(a):
    sys.stdout.write('(stdout) A: {!r}\n'.format(a))
    sys.stderr.write('(stderr) A: {!r}\n'.format(a))

capture = io.StringIO()                                                        #!!!

with redirect_stdout(capture), redirect_stderr(capture):
    misbehaving_function(5)

print(capture.getvalue())

"""
In this example, misbehaving_function() writes to both stdout and stderr,
but the two context managers send that output to the same io.StringIO instance
where it is saved to be used later.

Note

Both redirect_stdout() and redirect_stderr() modify global state
by replacing objects in the sys module, and should be used with care.
The functions are not thread-safe, and may interfere with other operations
that expect the standard output streams to be attached to terminal devices.
"""

#%%
#%%  Dynamic Context Manager Stacks
"""
Most context managers operate on one object at a time,
such as a single file or database handle.
In these cases, the object is known in advance and the code using the context manager
can be built around that one object.
In other cases, a program may need to create an unknown number of objects in a context,
while wanting all of them to be cleaned up when control flow exits the context.

ExitStack was created to handle these more dynamic cases.

An ExitStack instance maintains a stack data structure of cleanup callbacks.
The callbacks are populated explicitly within the context,
and any registered callbacks are called in the reverse order when control flow exits the context.
The result is like having multple nested with statements, except they are established dynamically.
"""

#%%  Stacking Context Managers
"""
There are several ways to populate the ExitStack.
This example uses .enter_context() method to add a new context manager to the stack.
"""
from contextlib import contextmanager, ExitStack

@contextmanager
def make_context(i):
    print('{} entering'.format(i))
    yield {}
    print('{} exiting'.format(i))

def variable_stack(n, msg='msg'):
    with ExitStack() as stack:
        for i in range(n):
            stack.enter_context(make_context(i))
            print(i)
        print(msg)

variable_stack(2, 'inside context')

#%%
"""
enter_context() first calls __enter__() on the context manager,
and then registers its __exit__() method as a callback to be invoked as the stack is undone.

0 entering
1 entering
inside context
1 exiting
0 exiting
"""
#%%
"""
The context managers given to ExitStack are treated as though
they are in a series of nested `with` statements.
Errors that happen anywhere within the context
propagate through the normal error handling of the context managers.
These context manager classes illustrate the way errors propagate.
"""
import contextlib

class Tracker:
    "Base class for noisy context managers."

    def __init__(self, i):
        self.i = i

    def msg(self, s):
        print('  {}({}): {}'.format(self.__class__.__name__, self.i, s))

    def __enter__(self):
        self.msg('entering')


class HandleError(Tracker):
    "If an exception is received, treat it as handled."

    def __exit__(self, *exc_details):
        received_exc = exc_details[1] is not None
        if received_exc:
            self.msg('handling exception {!r}'.format(exc_details[1]))
        self.msg('exiting {}'.format(received_exc))
        # Return Boolean value indicating whether the exception
        # was handled.
        return received_exc


class PassError(Tracker):
    "If an exception is received, propagate it."

    def __exit__(self, *exc_details):
        received_exc = exc_details[1] is not None
        if received_exc:
            self.msg('passing exception {!r}'.format(exc_details[1]))
        self.msg('exiting')
        # Return False, indicating any exception was not handled.
        return False


class ErrorOnExit(Tracker):
    "Cause an exception."

    def __exit__(self, *exc_details):
        self.msg('throwing error')
        raise RuntimeError('from {}'.format(self.i))


class ErrorOnEnter(Tracker):
    "Cause an exception."

    def __enter__(self):
        self.msg('throwing error on enter')
        raise RuntimeError('from {}'.format(self.i))

    def __exit__(self, *exc_info):
        self.msg('exiting')


def variable_stack(lst, msg='msg'):
    with ExitStack() as stack:
        for i in lst:
            stack.enter_context(i)
        print(msg)

#%%
"""
The examples using these classes are based around variable_stack(),
which uses the context managers passed to construct an ExitStack,
building up the overall context one by one.

The examples below pass different context managers to explore the error handling behavior.
First, the normal case of no exceptions.
"""
print('No errors:')
variable_stack([
    HandleError(1),
    PassError(2),
])

#%%
"""
Then, an example of handling exceptions within the context managers at the end of the stack,
in which all of the open contexts are closed as the stack is unwound.
"""
print('\nError at the end of the context stack:')
variable_stack([
    HandleError(1),
    HandleError(2),
    ErrorOnExit(3),
])

#%%
"""
Next, an example of handling exceptions within the context managers in the middle of the stack,
in which the error does not occur until some contexts are already closed,
so those contexts do not see the error.
"""
print('\nError in the middle of the context stack:')
variable_stack([
    HandleError(1),
    PassError(2),
    ErrorOnExit(3),
    HandleError(4),
])

#%%
"""
Finally, an example of the exception remaining unhandled and propagating up to the calling code.
"""
try:
    print('\nError ignored:')
    variable_stack([
        PassError(1),
        ErrorOnExit(2),
    ])
except RuntimeError:
    print('error handled outside of context')

#%%
"""
If any context manager in the stack receives an exception and returns a True value,
it prevents that exception from propagating up to any other context managers.
"""

#%% Arbitrary Context Callbacks
"""
ExitStack also supports arbitrary callbacks for closing a context,
making it easy to clean up resources that are not controlled via a context manager.
"""

def callback(*args, **kwds):
    print('closing callback({}, {})'.format(args, kwds))

with ExitStack() as stack:
    stack.callback(callback, 'arg1', 'arg2')
    stack.callback(callback, arg3='val3')

#%%
"""
Just as with the __exit__() methods of full context managers,
the callbacks are invoked in the reverse order that they are registered.
"""

closing callback((), {'arg3': 'val3'})
closing callback(('arg1', 'arg2'), {})

#%%
"""
The callbacks are invoked regardless of whether an error occurred,
and they are not given any information about whether an error occurred.
Their return value is ignored.
"""

def callback(*args, **kwds):
    print('closing callback({}, {})'.format(args, kwds))

try:
    with contextlib.ExitStack() as stack:
        stack.callback(callback, 'arg1', 'arg2')
        stack.callback(callback, arg3='val3')
        raise RuntimeError('thrown error')
except RuntimeError as err:
    print('ERROR: {}'.format(err))

#%%
"""
Because they do not have access to the error,
callbacks are unable to suppress exceptions from propagating
through the rest of the stack of context managers.
"""
#%%
"""
Callbacks make a convenient way to clearly define cleanup logic without
the overhead of creating a new context manager class.
To improve code readability, that logic can be encapsulated in an inline function,
and callback() can be used as a decorator.
"""
import contextlib


with ExitStack() as stack:

    @stack.callback
    def inline_cleanup():
        print('inline_cleanup()')
        print('local_resource = {!r}'.format(local_resource))

    local_resource = 'resource created in context'
    print('within the context')

#%%
"""
There is no way to specify the arguments for functions registered using the decorator form of callback().
However, if the cleanup callback is defined inline, scope rules give it access to variables defined in the calling code.
"""

#%%
#%% Partial Stacks
"""
Sometimes when building complex contexts it is useful to be able to abort an operation
if the context cannot be completely constructed,
but to delay the cleanup of all resources until a later time if they can all be set up properly.

For example, if an operation needs several long-lived network connections,
it may be best to not start the operation if one connection fails.
However, if all of the connections can be opened they need to stay open longer
than the duration of a single context manager.

The pop_all() method of ExitStack can be used in this scenario.

pop_all() clears all of the context managers and callbacks from the stack on which it is called,
and returns a new stack pre-populated with those same context managers and callbacks.
The close() method of the new stack can be invoked later,
after the original stack is gone, to clean up the resources.
"""
def variable_stack(contexts):
    with ExitStack() as stack:
        for c in contexts:
            stack.enter_context(c)
        # Return the close() method of a new stack as a clean-up
        # function.
        return stack.pop_all().close
    # Explicitly return None, indicating that the ExitStack could
    # not be initialized cleanly but that cleanup has already
    # occurred.
    return None


print('No errors:')
cleaner = variable_stack([
    HandleError(1),
    HandleError(2),
])
cleaner()

#%%
print('\nHandled error building context manager stack:')
try:
    cleaner = variable_stack([
        HandleError(1),
        ErrorOnEnter(2),
    ])
except RuntimeError as err:
    print('caught error {}'.format(err))
else:
    if cleaner is not None:
        cleaner()
    else:
        print('no cleaner returned')

#%%
print('\nUnhandled error building context manager stack:')
try:
    cleaner = variable_stack([
        PassError(1),
        ErrorOnEnter(2),
    ])
except RuntimeError as err:
    print('caught error {}'.format(err))
else:
    if cleaner is not None:
        cleaner()
    else:
        print('no cleaner returned')

#%%
"""
This example uses the same context manager classes defined earlier, with the difference that ErrorOnEnter produces an error on __enter__() instead of __exit__(). Inside variable_stack(), if all of the contexts are entered without error then the close() method of a new ExitStack is returned. If a handled error occurs, variable_stack() returns None to indicate that the cleanup work is already done. And if an unhandled error occurs, the partial stack is cleaned up and the error is propagated.
"""

No errors:
  HandleError(1): entering
  HandleError(2): entering
  HandleError(2): exiting False
  HandleError(1): exiting False

Handled error building context manager stack:
  HandleError(1): entering
  ErrorOnEnter(2): throwing error on enter
  HandleError(1): handling exception RuntimeError('from 2')
  HandleError(1): exiting True
no cleaner returned

Unhandled error building context manager stack:
  PassError(1): entering
  ErrorOnEnter(2): throwing error on enter
  PassError(1): passing exception RuntimeError('from 2')
  PassError(1): exiting
caught error from 2

#%%
#%%