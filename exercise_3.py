'''
Agenda:
1) Releasing resources and "with" statements
2) Context managers, enter and exit methods
3) Contextlib (decorator style context managers)
** Using git throughout!!
'''

# Exercise 3
# Nothing to do here, just know that ...
# there is more than one way to write a context manager!!

#https://docs.python.org/3/library/contextlib.html
from contextlib import contextmanager

@contextmanager
def managed_resource(*args, **kwds):
    # Code to acquire resource, e.g.:
    resource = acquire_resource(*args, **kwds)
    try:
        yield resource
    finally:
        # Code to release resource, e.g.:
        release_resource(resource)

with managed_resource(timeout=3600) as resource:
    # Resource is released at the end of this block,
    # even if code in the block raises an exception
