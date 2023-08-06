# encoding: utf-8
import os
import sys
import re
import json
import csv
from contextlib import contextmanager
from functools import cmp_to_key
from collections import OrderedDict, defaultdict
from os.path import abspath, dirname, exists, join, splitext
from random import choice, shuffle

from Foundation import NSAutoreleasePool
from AppKit import NSBundle
from plotdevice import DeviceError
from .readers import read, XMLParser, Element

__all__ = ('grid', 'random', 'shuffled', 'choice', 'ordered', 'order', 'files', 'read', 'autotext', '_copy_attr', '_copy_attrs', 'odict', 'ddict', 'adict')

### Utilities ###

def grid(cols, rows, colSize=1, rowSize=1, shuffled=False):
    """Returns an iterator that contains coordinate tuples.

    The grid can be used to quickly create grid-like structures. A common way to use them is:
        for x, y in grid(10,10,12,12):
            rect(x,y, 10,10)
    """
    # Prefer using generators.
    rowRange = range(int(rows))
    colRange = range(int(cols))
    # Shuffled needs a real list, though.
    if (shuffled):
        rowRange = list(rowRange)
        colRange = list(colRange)
        shuffle(rowRange)
        shuffle(colRange)
    for y in rowRange:
        for x in colRange:
            yield (x*colSize,y*rowSize)

def random(v1=None, v2=None, mean=None, sd=None):
    """Returns a random value.

    This function does a lot of things depending on the parameters:
    - If one or more floats is given, the random value will be a float.
    - If all values are ints, the random value will be an integer.

    - If one value is given, random returns a value from 0 to the given value.
      This value is not inclusive.
    - If two values are given, random returns a value between the two; if two
      integers are given, the two boundaries are inclusive.
    """
    import random
    if v1 != None and v2 == None: # One value means 0 -> v1
        if isinstance(v1, float):
            return random.random() * v1
        else:
            return int(random.random() * v1)
    elif v1 != None and v2 != None: # v1 -> v2
        if isinstance(v1, float) or isinstance(v2, float):
            start = min(v1, v2)
            end = max(v1, v2)
            return start + random.random() * (end-start)
        else:
            start = min(v1, v2)
            end = max(v1, v2) + 1
            return int(start + random.random() * (end-start))
    elif mean != None and sd!= None:
        return random.normalvariate(mean, sd)
    else: # No values means 0.0 -> 1.0
        return random.random()

def files(path="*", case=True):
    """Returns a list of files.

    You can use wildcards to specify which files to pick, e.g.
        f = files('~/Pictures/*.jpg')

    For a case insensitive search, call files() with case=False
    """
    from .iglob import iglob
    # if type(path)==unicode:
    #     path.encode('utf-8')
    path = os.path.expanduser(path)

    return list(iglob(path, case=case))

def autotext(sourceFile):
    from plotdevice.util.kgp import KantGenerator
    k = KantGenerator(sourceFile)
    return k.output()

### Permutation sugar ###

def _as_sequence(seq):
    if not hasattr(seq, '__getitem__'):
        badtype = 'ordered, shuffled, and friends only work for strings, tuples and lists (not %s)' % type(seq)
        raise DeviceError(badtype)
    return list(seq)

def _as_before(orig, lst):
    return "".join(lst) if isinstance(orig, str) else list(lst)

def _key(seq, names):
    # treat objects without a given key and objects with the key set to None equivalently
    MISSING = None

    # look for dict items by default
    getter = lambda obj: tuple(obj.get(n, MISSING) for n in names)

    # walk through the objects and see if any of them lacks the dict fields but has attrs
    for obj in seq:
        try:
            if any(n in obj for n in names):
                break # dict fields exist so use the itemgetter
        except TypeError:
            # for non-dict objects like namedtuples and dataclasses use an attrgetter
            if any(hasattr(obj, n) for n in names):
                getter = lambda obj: tuple(getattr(obj, n, MISSING) for n in names)

    def compare(a, b):
        default = 0
        try:
            a = getter(a)
            b = getter(b)
            if a > b: return 1
            if a < b: return -1
        except TypeError:
            for aa, bb in zip(a, b):
                if aa is MISSING and bb is MISSING: return default
                if aa is MISSING: return default or 1
                if bb is MISSING: return default or -1
                if aa > bb: default = 1
                if aa < bb: default = -1
        return default

    return cmp_to_key(compare)

def order(seq, *names, **kwargs):
    lst = _as_sequence(seq)
    if not names or not seq:
        reordered = [(it,idx) for idx,it in enumerate(lst)]
    else:
        key = _key(lst, names)
        reordered = [(key(it), idx) for idx,it in enumerate(lst)]
    reordered.sort(**kwargs)
    return [it[1] for it in reordered]

def ordered(seq, *names, **kwargs):
    """Return a sorted copy of a list or tuple, optionally using a common item or
    attr name of the elements within the sequence.

    If included, *names should be one or more strings indicating which `fields` of
    the sequence elements should be used in comparing their equality. If more than
    one name is specified, the second field will be used to break `ties' based on
    the first.

    The return value will be ordered in an ascending fashion, but can be flipped
    using the reverse=True keyword argument."""
    lst = _as_sequence(seq)
    if kwargs.get('perm') and lst:
        return _as_before(seq, [lst[idx] for idx in kwargs['perm']])

    if not names or not lst:
        return _as_before(seq, sorted(lst, **kwargs))
    return _as_before(seq, sorted(lst, key=_key(lst, names), **kwargs))

def shuffled(seq):
    """Returns a random permutation of a list or tuple (without modifying the original)"""
    lst = _as_sequence(seq)
    shuffle(lst)
    return _as_before(seq, lst)

### deepcopy helpers ###

def _copy_attr(v):
    if v is None:
        return None
    elif hasattr(v, "copy"):
        return v.copy()
    elif isinstance(v, tuple):
        if hasattr(v, '_fields'):
            return v._replace() # don't demote namedtuples to tuples
        return tuple(v)
    elif isinstance(v, list):
        return list(v)
    elif isinstance(v, (int, str, float, bool)):
        return v
    else:
        raise DeviceError("Don't know how to copy '%s'." % v)

def _copy_attrs(source, target, attrs):
    for attr in attrs:
        try:
            setattr(target, attr, _copy_attr(getattr(source, attr)))
        except AttributeError as e:
            print("missing attr: %r"% attr, hasattr(source, attr), hasattr(target, attr))
            raise e

### tuple/list de-nester ###

def _flatten(seq):
    return sum( ([x] if not isinstance(x, (list,tuple)) else list(x) for x in seq), [] )

### repr decorator (tidies numbers) ###

def trim_zeroes(func):
    return lambda slf: re.sub(r'\.?0+(?=[,\)\]])', '', func(slf))

### Dimension-aware number detector (replacement for isintance) ###

def numlike(obj):
    return hasattr(obj, '__int__') or hasattr(obj, '__float__')

### give ordered- and default-dict a nicer repr ###

class BetterRepr(object):
    def __repr__(self, indent=2):
        result = '%s{'%self.__class__.__name__
        for k,v in self.iteritems():
            if isinstance(v, BetterRepr):
                vStr = v.__repr__(indent + 2)
            else:
                vStr = v.__repr__()
            result += "\n" + ' '*indent + k.__repr__() + ': ' + vStr
        if not result.endswith('{'):
            result += "\n"
        result += '}'
        return result

class odict(BetterRepr,OrderedDict):
    """Dictionary that remembers insertion order

    Normal dict objects return keys in an arbitrary order. An odict will return them in
    the order you add them. To initialize an odict and not lose the ordering in the process,
    avoid using keyword arguments and instead pass a list of (key,val) tuples:

        odict([ ('foo',12), ('bar',14), ('baz', 33) ])

    or as part of a generator expression:

        odict( (k,other[k]) for k in sorted(other.keys()) )

    """
    pass

class ddict(BetterRepr,defaultdict):
    """Dictionary with default factory

    Any time you access a key that was previously undefined, the factory function
    is called and a default value is inserted in the dictionary. e.g.,

        normal_dict = {}
        normal_dict['foo'].append(42) # raises a KeyError

        lst_dict = ddict(list)
        lst_dict['foo'].append(42)    # sets 'foo' to [42]

        num_dict = ddict(int)
        print num_dict['bar']         # prints '0'
        num_dict['baz'] += 2          # increments 'baz' from 0 to 2

    """
    pass

### the not very pythonic but often convenient dot-notation dict ###

class adict(BetterRepr, dict):
    """A dictionary object whose items may also be accessed with dot notation.

    Items can be assigned using dot notation even if a dictionary method of the
    same name exists. Subsequently, dot notation will still reference the method,
    but the assigned value can be read out using traditional `d["name"]` syntax.
    """
    def __init__(self, *args, **kw):
        super(adict, self).__init__(*args, **kw)
        self.__initialised = True

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as k:
            raise AttributeError(k)

    def __setattr__(self, key, value):
        # this test allows attributes to be set in the __init__ method
        if '_adict__initialised' not in self.__dict__:
            return dict.__setattr__(self, key, value)
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError as k:
            raise AttributeError(k)


### autorelease pool manager ###

@contextmanager
def autorelease():
    pool = NSAutoreleasePool.alloc().init()
    yield
    del pool


### module data dir ###

def rsrc_path(resource=None):
    """Return absolute path of the rsrc directory (or a file within it)"""
    mod_root = abspath(dirname(dirname(__file__)))
    app_root = NSBundle.mainBundle().bundlePath()
    mod_rsrc = join(mod_root, 'rsrc')
    app_rsrc = join(app_root, 'Contents/Resources')
    src_rsrc = join(mod_root, '../app/Resources')

    for rsrc_root in (mod_rsrc, app_rsrc, src_rsrc):
        if exists("%s/colors.json" % rsrc_root): # check for a known rsrc file
            break
    else:
        raise RuntimeError("Couldn't locate resources directory.")

    if resource:
        return join(rsrc_root, resource)
    return rsrc_root
