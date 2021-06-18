# reference : https://kimdoky.github.io/python/2019/11/24/python-itertools/
# https://docs.python.org/ko/3.7/library/itertools.html


from itertools import islice
from itertools import chain
import collections
from itertools import count


def take(n, iterable):
    # refurn first n items of the iterable as a list
    return list(islice(iterable, n))


def prepend(value, iterator):
    # prepend a single value in front of an iterator
    return chain([value], iterator)


def tail(n, iterable):
    # return an iterator over the last n items
    return iter(collections.deque(iterable, maxlen=n))


def tabulate(function, start=0):
    # return function(0), function(1), ...
    return map(function, count(start))


def consume(iterator, n=None):
    # advance the iterator n-steps ahead. if n is None, consume entirely.
    if n is None:
        collections.deque(iterator, maxlen=0)
    else:
        next(islice(iterator, n, n), None)


def nth(iterable, n, default=None):
    # returns the nth item or a default value
    return next(islice(iterable, n, None), default)


def all_equal(iterable):
    # returns True if all the elements are equal to each other
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


def quantify(iterable, pred=bool):
    # count how many times the predicate is true
    return sum(map(pred, iterable))


def padnone(iterable):
    # return the sequence elements and then returns None indefinitely.
    # useful for emulating the behaviour of the built-in map() function.
    return chain(iterable, repeat(None))


def ncycles(iterables, n):
    # return the sequence elements n times
    return chain.from_iterable(repeat(tuple(iterable), n))


def dotproduct(vec1, vec2):
    return sum(map(operator.mul, vec1, vec2))


def flatten(listOfLists):
    # Flatten one level of nesting
    return chain.from_iterable(listOfLists)


def repeatfunc(func, times=None, *args):
    # Repeat calls to func with specified arguments.
    # ex. repeawtfunc(random.random)
    if times is None:
        return starmap(func, repeat(args))
    return starmap(func, repeat(args, times))


iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print(take(4, iterable))  # 1, 2, 3, 4

print(prepend([11, 12], iterable))
# <itertools.chain object at 0x7fd236c418e0>

for i in prepend([11, 12], iterable):
    print(i)
# [11, 12], 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

print(tail(3, iterable))
# <_collections._deque_iterator object at 0x7ffa286256d0>

for i in tail(3, iterable):
    print(i)
# 8, 9, 10

print(tabulate(take, start=0))
# <map object at 0x7fe4e2c41940>

print(consume(iterable))
