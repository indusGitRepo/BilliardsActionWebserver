

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _phylib
else:
    import _phylib

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "this":
            set(self, name, value)
        elif name == "thisown":
            self.this.own(value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


PHYLIB_BALL_RADIUS = _phylib.PHYLIB_BALL_RADIUS
PHYLIB_BALL_DIAMETER = _phylib.PHYLIB_BALL_DIAMETER
PHYLIB_HOLE_RADIUS = _phylib.PHYLIB_HOLE_RADIUS
PHYLIB_TABLE_LENGTH = _phylib.PHYLIB_TABLE_LENGTH
PHYLIB_TABLE_WIDTH = _phylib.PHYLIB_TABLE_WIDTH
PHYLIB_SIM_RATE = _phylib.PHYLIB_SIM_RATE
PHYLIB_VEL_EPSILON = _phylib.PHYLIB_VEL_EPSILON
PHYLIB_DRAG = _phylib.PHYLIB_DRAG
PHYLIB_MAX_TIME = _phylib.PHYLIB_MAX_TIME
PHYLIB_MAX_OBJECTS = _phylib.PHYLIB_MAX_OBJECTS
PHYLIB_STILL_BALL = _phylib.PHYLIB_STILL_BALL
PHYLIB_ROLLING_BALL = _phylib.PHYLIB_ROLLING_BALL
PHYLIB_HOLE = _phylib.PHYLIB_HOLE
PHYLIB_HCUSHION = _phylib.PHYLIB_HCUSHION
PHYLIB_VCUSHION = _phylib.PHYLIB_VCUSHION
class phylib_coord(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    x = property(_phylib.phylib_coord_x_get, _phylib.phylib_coord_x_set)
    y = property(_phylib.phylib_coord_y_get, _phylib.phylib_coord_y_set)

    def __init__(self, x, y):
        _phylib.phylib_coord_swiginit(self, _phylib.new_phylib_coord(x, y))
    __swig_destroy__ = _phylib.delete_phylib_coord

# Register phylib_coord in _phylib:
_phylib.phylib_coord_swigregister(phylib_coord)
class phylib_still_ball(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    number = property(_phylib.phylib_still_ball_number_get, _phylib.phylib_still_ball_number_set)
    pos = property(_phylib.phylib_still_ball_pos_get, _phylib.phylib_still_ball_pos_set)

    def __init__(self):
        _phylib.phylib_still_ball_swiginit(self, _phylib.new_phylib_still_ball())
    __swig_destroy__ = _phylib.delete_phylib_still_ball

# Register phylib_still_ball in _phylib:
_phylib.phylib_still_ball_swigregister(phylib_still_ball)
class phylib_rolling_ball(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    number = property(_phylib.phylib_rolling_ball_number_get, _phylib.phylib_rolling_ball_number_set)
    pos = property(_phylib.phylib_rolling_ball_pos_get, _phylib.phylib_rolling_ball_pos_set)
    vel = property(_phylib.phylib_rolling_ball_vel_get, _phylib.phylib_rolling_ball_vel_set)
    acc = property(_phylib.phylib_rolling_ball_acc_get, _phylib.phylib_rolling_ball_acc_set)

    def __init__(self):
        _phylib.phylib_rolling_ball_swiginit(self, _phylib.new_phylib_rolling_ball())
    __swig_destroy__ = _phylib.delete_phylib_rolling_ball

# Register phylib_rolling_ball in _phylib:
_phylib.phylib_rolling_ball_swigregister(phylib_rolling_ball)
class phylib_hole(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    pos = property(_phylib.phylib_hole_pos_get, _phylib.phylib_hole_pos_set)

    def __init__(self):
        _phylib.phylib_hole_swiginit(self, _phylib.new_phylib_hole())
    __swig_destroy__ = _phylib.delete_phylib_hole

# Register phylib_hole in _phylib:
_phylib.phylib_hole_swigregister(phylib_hole)
class phylib_hcushion(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    y = property(_phylib.phylib_hcushion_y_get, _phylib.phylib_hcushion_y_set)

    def __init__(self):
        _phylib.phylib_hcushion_swiginit(self, _phylib.new_phylib_hcushion())
    __swig_destroy__ = _phylib.delete_phylib_hcushion

# Register phylib_hcushion in _phylib:
_phylib.phylib_hcushion_swigregister(phylib_hcushion)
class phylib_vcushion(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    x = property(_phylib.phylib_vcushion_x_get, _phylib.phylib_vcushion_x_set)

    def __init__(self):
        _phylib.phylib_vcushion_swiginit(self, _phylib.new_phylib_vcushion())
    __swig_destroy__ = _phylib.delete_phylib_vcushion

# Register phylib_vcushion in _phylib:
_phylib.phylib_vcushion_swigregister(phylib_vcushion)
class phylib_untyped(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    still_ball = property(_phylib.phylib_untyped_still_ball_get, _phylib.phylib_untyped_still_ball_set)
    rolling_ball = property(_phylib.phylib_untyped_rolling_ball_get, _phylib.phylib_untyped_rolling_ball_set)
    hole = property(_phylib.phylib_untyped_hole_get, _phylib.phylib_untyped_hole_set)
    hcushion = property(_phylib.phylib_untyped_hcushion_get, _phylib.phylib_untyped_hcushion_set)
    vcushion = property(_phylib.phylib_untyped_vcushion_get, _phylib.phylib_untyped_vcushion_set)

    def __init__(self):
        _phylib.phylib_untyped_swiginit(self, _phylib.new_phylib_untyped())
    __swig_destroy__ = _phylib.delete_phylib_untyped

# Register phylib_untyped in _phylib:
_phylib.phylib_untyped_swigregister(phylib_untyped)
class phylib_object(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    type = property(_phylib.phylib_object_type_get, _phylib.phylib_object_type_set)
    obj = property(_phylib.phylib_object_obj_get, _phylib.phylib_object_obj_set)

    def __init__(self, type, num, pos, vel, acc, x, y):
        _phylib.phylib_object_swiginit(self, _phylib.new_phylib_object(type, num, pos, vel, acc, x, y))

    def __str__(self):
        return _phylib.phylib_object___str__(self)
    __swig_destroy__ = _phylib.delete_phylib_object

# Register phylib_object in _phylib:
_phylib.phylib_object_swigregister(phylib_object)
class phylib_table(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    time = property(_phylib.phylib_table_time_get, _phylib.phylib_table_time_set)
    object = property(_phylib.phylib_table_object_get, _phylib.phylib_table_object_set)

    def __init__(self):
        _phylib.phylib_table_swiginit(self, _phylib.new_phylib_table())

    def copy(self):
        return _phylib.phylib_table_copy(self)

    def segment(self):
        return _phylib.phylib_table_segment(self)

    def get_object(self, i):
        return _phylib.phylib_table_get_object(self, i)

    def add_object(self, object1):
        return _phylib.phylib_table_add_object(self, object1)
    __swig_destroy__ = _phylib.delete_phylib_table

# Register phylib_table in _phylib:
_phylib.phylib_table_swigregister(phylib_table)

def phylib_new_still_ball(number, pos):
    return _phylib.phylib_new_still_ball(number, pos)

def phylib_new_rolling_ball(number, pos, vel, acc):
    return _phylib.phylib_new_rolling_ball(number, pos, vel, acc)

def phylib_new_hole(pos):
    return _phylib.phylib_new_hole(pos)

def phylib_new_hcushion(y):
    return _phylib.phylib_new_hcushion(y)

def phylib_new_vcushion(x):
    return _phylib.phylib_new_vcushion(x)

def phylib_new_table():
    return _phylib.phylib_new_table()

def phylib_copy_object(dest, src):
    return _phylib.phylib_copy_object(dest, src)

def phylib_copy_table(table):
    return _phylib.phylib_copy_table(table)

def phylib_add_object(table, object):
    return _phylib.phylib_add_object(table, object)

def phylib_free_table(table):
    return _phylib.phylib_free_table(table)

def phylib_sub(c1, c2):
    return _phylib.phylib_sub(c1, c2)

def phylib_length(c):
    return _phylib.phylib_length(c)

def phylib_dot_product(a, b):
    return _phylib.phylib_dot_product(a, b)

def phylib_distance(obj1, obj2):
    return _phylib.phylib_distance(obj1, obj2)

def phylib_roll(new, old, time):
    return _phylib.phylib_roll(new, old, time)

def phylib_stopped(object):
    return _phylib.phylib_stopped(object)

def phylib_bounce(a, b):
    return _phylib.phylib_bounce(a, b)

def phylib_rolling(t):
    return _phylib.phylib_rolling(t)

def phylib_segment(table):
    return _phylib.phylib_segment(table)

def phylib_object_string(object):
    return _phylib.phylib_object_string(object)

