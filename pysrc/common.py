import wireviz
from wireviz.DataClasses import \
  Options, Tweak, Image, AdditionalComponent, Connector, \
  Cable, Connection, MatePin, MateComponent

class Group:
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
  # we could use asdict here, 
  # but still should remove the 'name' entry
  return { thing.__dict__['name'] :
    { k: v for k, v in thing.__dict__.items()
      if k not in {'name' }
    }
  }

# make our own class wrappers for cable, conectors, and connections
def cableclass(cls):
  kind = 'cable'
  def __post_init__(self): pass
  def __init__(self, name, *args, **kw):
    super(cls,self).__init__( name, **{ **cls.defaults, **kw } )
  def dict(self): return wvdict(self)
  setattr(cls, 'kind', kind )
  setattr(cls, '__post_init__', __post_init__ )
  setattr(cls, '__init__', __init__ )
  setattr(cls, 'dict', dict )
  return cls


