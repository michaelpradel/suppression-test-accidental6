"""
Toy example.
"""

def hello():
    """ A fantastic docstring,
        which even spans two lines. """
    # pylint: disable=missing-format-string-key
    print("Hello %(first)s %(last)s" % {"First": "John", "last": "Doe"})
