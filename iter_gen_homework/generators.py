from typing import Iterable, Generator


def simple_generator(iterable: Iterable) -> Generator:
    yield from iterable


def reversed_generator(iterable: Iterable) -> Generator:
    yield from iterable[::-1]


def cycle_generator(iterable: Iterable) -> Generator:       # ???
    while True:
        # try:
        yield from iterable
        # except StopIteration:
        #     pass


def ping_pong_generator(iterable: Iterable) -> Generator:
    yield iterable[0]
    while True:
        yield from iterable[1::1]
        yield from iterable[1::-1]


if __name__ == "__main__":

    a = [0, 1, 2]

    generator = simple_generator(a)
    b = list(generator)
    assert b == [0, 1, 2]

    generator = reversed_generator(a)
    b = list(generator)
    assert b == [2, 1, 0]

    generator = cycle_generator(a)
    b = [next(generator) for _ in range(14)]
    assert b == [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1]

    generator = ping_pong_generator(a)
    b = [next(generator) for _ in range(14)]
    assert b == [0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1]
