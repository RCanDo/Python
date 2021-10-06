# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 10:49:38 2019
@author: kasprark
sources: 
    link: https://www.toptal.com/python/python-design-patterns
    chapter: Decorators
    author: 
        name: Andrei Boyanov
"""

#%%

users_actions = {'ak': ['+', '-'], 'xy': ['/', '*']}

def run(action: str, *args):
    try:
        a, b = args[:2]
    except:
        a, b = 3, 2
    print(action)
    if action == '+':
        return a + b
    elif action == '-':
        return a - b
    elif action == '/':
        return a / b
    elif action == '*':
        return a * b
    else:
        raise Exception('`action` not recognized!')

#%%
def execute0(user: str, action: str, *args, **kwargs):
    return run(action, *args)

execute0('ak', '+')
execute0('ak', '-', 3, 4)

execute0('qq', '+')
## ooops!, there is no authentication and authorization...


#%%

def authenticate(user: str):
    return user in users_actions.keys()

def authorize(user: str, action: str):
    return action in users_actions[user]

#check
authenticate('ak')
authorize('ak', '+')

authenticate('qq')
authorize('ak', '/')


#%%
def execute1(user, action, *args, **kwargs):
    if authenticate(user) and authorize(user, action):
        return run(action, *args)
    else:
        raise Exception('access denied!')

#check
execute1('ak', '+')
execute1('ak', '-', 3, 4)
execute1('xy', '/', 3, 4)


execute1('qq', '+')
execute1('ak', '/')
execute1('xy', '+')


#%%

"""
What is not so good here is that the execute function does much more than executing something. 
We are not following the single responsibility principle to the letter.

We can implement any authorization and authentication functionality in another place, 
in a decorator, like so:
"""

def execute2(action: str, *args):
    return run(action, *args)

def authenticated(fun):
    def decorated(*args):
        if authenticate(args[0]):
            return fun(*args)
        else:
            raise Exception('UnauthenticatedError')
    return decorated

def authorized(fun):
    def decorated(*args):
        if authorize(*args[:2]):
            return fun(*args[1:])
        else:
            raise Exception('UnauthorizedError')
    return decorated


## KEEP THE ORDER! -- it's reversed here!
execute2 = authorized(execute2)     # this runs SECOND 
execute2 = authenticated(execute2)  # this runs FIRST

"""
Now the execute() function is:
    Simple to read
    Does only one thing (at least when looking at the code)
    Is decorated with authentication
    Is decorated with authorization
"""

#%%

#check
execute2('ak', '+')
execute2(user='ak', action='+')  # TypeError: decorated() got an unexpected keyword argument 'user'

execute2('ak', '-', 3, 4)
execute2('xy', '/', 3, 4)

execute2('qq', '+')  # Exception: UnauthenticatedError -- OK!
execute2('ak', '/')  # Exception: UnauthorizedError -- OK!
execute2('xy', '+')  # Exception: UnauthorizedError -- OK!

#%%
"""
We write the same using Python’s integrated decorator syntax:
"""

## KEEP THE ORDER!

@authenticated  # this runs FIRST
@authorized     # this runs SECOND 
def execute(action, *args):
    return run(action, *args)

#%%

#check
execute('ak', '+')
execute(user='ak', action='+')  # TypeError: decorated() got an unexpected keyword argument 'user'

execute('ak', '-', 3, 4)
execute('xy', '/', 3, 4)

execute('qq', '+')  # Exception: UnauthenticatedError -- OK!
execute('ak', '/')  # Exception: UnauthorizedError -- OK!
execute('xy', '+')  # Exception: UnauthorizedError -- OK!

"""
It is important to note that you are not limited to functions as decorators. 
A decorator may involve entire classes. 
The only requirement is that they must be callables. 
But we have no problem with that; we just need to define the __call__(self) method.

You may also want to take a closer look at Python’s functools module. 
There is much to discover there!
"""

#%%
"""
It's still not clear how to use **kwargs.
After all writing decorators is pretty delicate matter just because of juggling with arguments.
"""

