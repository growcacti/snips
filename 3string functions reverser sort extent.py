


def reverse(o):
    t = type(o)
    if t in (str, tuple):
        n = list(o)
    else:
        n = o.copy()
    n.reverse()
    if t == str:
        return ''.join(n)
    elif t == tuple:
        return tuple(n)
    else:
        return n


def sort(o):
    t = type(o)
    if t in (str, tuple):
        n = list(o)
    else:
        n = o.copy()
    n.sort()
    if t == str:
        return ''.join(n)
    elif t == tuple:
        return tuple(n)
    else:
        return n



def extend(o, o1):
    t = type(o)
    if t in (str, tuple):
        n = list(o)
    else:
        n = o.copy()
    n.extend(o1)
    if t == str:
        return ''.join(n)
    elif t == tuple:
        return tuple(n)
    else:
        return n




