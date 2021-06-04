"""
For an excellent article on decorators see:
Primer on Python Decorators:  https://realpython.com/primer-on-python-decorators/


Boilerplate template for building a decorator for the article

import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator

"""


import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])


# A simple program that uses a decorator to register functions.

import random
PLUGINS = dict()

# This allows use to register functions using a dictionary
def register(func): 
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
	return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

@register
def say_yo(name):
	return f'Yo {name}, be my bro.'

# We want to use choose one of the above functions at random.
print(f'{list(PLUGINS.items())=}')
for i in range(10):
	print(30*'*')
	print(randomly_greet('Alex'))
	print(30*'*')