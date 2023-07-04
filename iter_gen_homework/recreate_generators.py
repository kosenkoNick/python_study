def my_zip(*iterables):
    """
    zip(*iterables) --> zip object

    Return a zip object whose .__next__() method returns a tuple where
    the i-th element comes from the i-th iterable argument.  The .__next__()
    method continues until the shortest iterable in the argument sequence
    is exhausted, and then it raises StopIteration.
    """
    iterators_list = [iter(itrbl) for itrbl in iterables]

    while True:
        try:
            yield tuple([next(itr) for itr in iterators_list])
        except StopIteration:
            break


def my_enumerate(iterable, start=0):
    """
    Return an enumerate object.

      iterable
        an object supporting iteration

    The enumerate object yields pairs containing a count (from start, which
    defaults to zero) and a value yielded by the iterable argument.

    enumerate is useful for obtaining an indexed list:
        (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
    """
    for item in iterable:
        yield start, item
        start += 1


def my_filter(key, iterable):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    for item in iterable:
        if key is None:
            if item:
                yield item
        else:
            if key(item):
                yield item


def my_map(func, *iterables):
    """
    map(func, *iterables) --> map object

    Make an iterator that computes the function using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.
    """
    iterators_list = [iter(itrbl) for itrbl in iterables]

    while True:
        try:
            yield func(*[next(itr) for itr in iterators_list])
        except StopIteration:
            break


if __name__ == "__main__":

    a = ["a", "b", "c"]
    b = ["x", "y", "z"]

    assert list(zip(a, b)) == [("a", "x"), ("b", "y"), ("c", "z")]
    assert list(zip(a)) == [("a",), ("b",), ("c",)]
    assert list(my_zip(a, b)) == [("a", "x"), ("b", "y"), ("c", "z")]
    assert list(my_zip(a)) == [("a",), ("b",), ("c",)]

    assert list(enumerate(a)) == [(0, "a"), (1, "b"), (2, "c")]
    assert list(enumerate(a, start=2)) == [(2, "a"), (3, "b"), (4, "c")]
    assert list(my_enumerate(a)) == [(0, "a"), (1, "b"), (2, "c")]
    assert list(my_enumerate(a, start=2)) == [(2, "a"), (3, "b"), (4, "c")]

    a = [0, 1, 2, 0, 2, 3]
    assert list(filter(None, a)) == [1, 2, 2, 3]
    assert list(filter(lambda i: i < 2, a)) == [0, 1, 0]
    assert list(my_filter(None, a)) == [1, 2, 2, 3]
    assert list(my_filter(lambda i: i < 2, a)) == [0, 1, 0]

    a = [0, 1, 2, 0, 2, 3]
    b = [3, 1, 2, 2, 1, 4]
    add = lambda frst, scnd: frst + scnd

    assert list(map(str, a)) == ["0", "1", "2", "0", "2", "3"]
    assert list(map(add, a, b)) == [3, 2, 4, 2, 3, 7]

    assert list(my_map(str, a)) == ["0", "1", "2", "0", "2", "3"]
    assert list(my_map(add, a, b)) == [3, 2, 4, 2, 3, 7]
