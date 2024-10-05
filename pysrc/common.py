from dataclasses import asdict
import wireviz
from wireviz.DataClasses import \
  Options, Tweak, Image, AdditionalComponent, Connector, \
  Cable, Connection, MatePin, MateComponent

class Group:
  '''Builds dictionary of cables / connectors for parsing.'''
  def __init__(self, label, *args):
    self.label = label
    self.items = {}
    self.add(*args)
  def add(self, *args):
    for arg in args:
      self.items.update( arg.dict() )
  def dict(self):
    return { self.label : self.items }

def wvdict( thing ):
  return { thing.__dict__['name'] :
    { k: v for k, v in thing.__dict__.items()
      if k not in {'name' }
    }
  }

# tried using asdict, still should remove 'name' entry
# this causes an error with the subsequent parsing
# it seems to be how some fields in the dictionaries are
# being represented differently. 
# The image field specifically causes the error:
#   asdict     'image': {'src': 'images/picoblade-51021-07-socket.png'
#   __dict__   'image': Image(src='images/picoblade-51021-07-socket.png'
# Also some, not all, of the entries are expressed differently:
#   asdict     'scale': 'false'
#   __dict__   scale='false'
def wvdict_not_working_now( thing ):
  d = asdict(thing)
  return { 
    d['name']: { k: v for k, v in d.items() if k not in {'name'}} 
  }

# make class wrappers for cable, conectors, and connections
# don't have to manually add all the boiler-plate to each class
# see example in cables.py
def wirevizclass(cls):
  # remove post init function from the class,
  # we only want the initial fields and not derived ones
  def __post_init__(self): pass
  def __init__(self, name, *args, **kw):
    # initialize wireviz class, combining defaults and passed args
    super(cls,self).__init__( name, **{ **cls.defaults, **kw } )
  # function to return dictionary in format needed for parse
  def dict(self): return wv2dict(self)
  setattr(cls, '__post_init__', __post_init__ )
  setattr(cls, '__init__', __init__ )
  setattr(cls, 'dict', dict )
  return cls

def cableclass(cls):
  kind = 'cable'
  setattr(cls, 'kind', kind )
  return wirevizclass(cls)

def connectorclass(cls):
  kind = 'connector'
  setattr(cls, 'kind', kind )
  return wirevizclass(cls)


