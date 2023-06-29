class SimpleIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __next__(self):
        try:
            val = self.iterable[self.index]
            self.index += 1
            return val
        except Exception:
            raise StopIteration

    def __iter__(self):
        return self


class ReversedIterator:

    def __init__(self, iterable):
        self.iterable = iterable

    def __next__(self):
        ...

    def __iter__(self):
        yield from self.iterable[::-1]


class CycleIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __next__(self):
        val = self.iterable[self.index]
        self.index = 0 if self.index == len(self.iterable) - 1 else self.index + 1
        return val

    def __iter__(self):
        return self


class PingPongIterator:

    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __next__(self):
        val = self.iterable[self.index]

        if self.index == len(self.iterable) - 1:
            self.iterable = self.iterable[::-1]
            self.index = 0

        self.index += 1

        return val

    def __iter__(self):
        return self


if __name__ == "__main__":
    a = [0, 1, 2]

    iterator = SimpleIterator(a)
    b = list(iterator)
    assert b == [0, 1, 2]

    iterator = ReversedIterator(a)
    b = list(iterator)
    assert b == [2, 1, 0]

    iterator = CycleIterator(a)
    b = [next(iterator) for _ in range(14)]
    assert b == [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1]

    iterator = PingPongIterator(a)
    b = [next(iterator) for _ in range(14)]
    assert b == [0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1]
