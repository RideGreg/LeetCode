# https://stackoverflow.com/questions/661603/how-do-i-know-if-a-generator-is-empty-from-the-start
# https://stackoverflow.com/questions/1966591/hasnext-in-python-iterators
import itertools
def hasNext(iterator):
    try:
        first = next(iterator)
    except StopIteration:
        return False, iter([])
    return True, itertools.chain([first], iterator)

it = iter(range(3))
for _ in range(5):
    has_next, it = hasNext(it)
    if has_next:
        print(next(it))
    else:
        print('no next')