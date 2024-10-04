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
  # return key, value pair
  #return thing.__dict__['name'],  \
  #  { k: v for k, v in thing.__dict__.items()
  #    if k not in {'name', 'bgcolor', 'bgcolor_title'} 
  #  }
  # return dict
  if thing.kind == 'cable':
    gauge = f"{thing.__dict__['gauge']} {thing.__dict__['gauge_unit']}"
    thing.__dict__['gauge_unit'] = None
    thing.__dict__['gauge'] = gauge

  return { thing.__dict__['name'] :
    { k: v for k, v in thing.__dict__.items()
      if k not in {'name', 'bgcolor', 'bgcolor_title', \
          'ports_left', 'ports_right', 'visible_pins', \
          'connections', 'gauge_unit'
          } 
    }
  }
