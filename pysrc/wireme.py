#!/usr/bin/env python

from pathlib import Path
from wireviz import wireviz
#from wireviz.DataClasses import \
#  Options, Tweak, Image, AdditionalComponent, Connector, \
#  Cable, Connection, MatePin, MateComponent
from connectors import *
from cables import *

'''Example trying to use wireviz python library directly.'''

w1j1 = PICOBLADE_7S( 
  'W1J1', 
  pinlabels = [ 
    'VIN-', 'VIN+', 'OUT_COM', 
    'OUT4', 'OUT3', 'OUT2', 'OUT1', 
  ]
)

w1j2 = PICOBLADE_8S( 
  'W1J2',
  pinlabels = [ 
      'INP1', 'INP2', 'INP3', 'INP4', 'INP_COM', 
      'XTXD', 'XRXD', 'XGND', 
  ]
)

w1j3 = JST_SMR_18S( 
  'W1J3',
   pinlabels = [ 
      'XRXD', 'XTXD', 'XGND', 
      'INP_COM', 'OUT_COM',
      'OUT1', 'OUT2', 'OUT3', 'OUT4', 
      'VIN+', 'VIN-',
      'INP1', 'INP2', 'INP3', 'INP4', 
  ]
)

w1 = CABLE_ADM2704_26(
    'W1',
    length =  2,
    wirecount =  16,
    colors = [ 
      'GNBK', 'WH',
      'GN',   'BU', 'VT', 'GY', 'YE', 
      'WHBK', 'OG', 'BUWH', 'RDWH', 'YEBK', 
      'BN',   'BK', 'RD', 
      'OGBK', 'GYBK', 'VTBK',
    ],
    wirelabels = [ 
      'VIN-', 'VIN+', 
      'OUT_COM', 'OUT4', 'OUT3', 'OUT2', 'OUT1', 
      'INP1', 'INP2', 'INP3', 'INP4', 'INP_COM', 
      'XTXD', 'XRXD', 'XGND',
   ]
)

# connections:
#   -
#     - W1J1: [ VIN-, VIN+, OUT_COM, OUT4, OUT3, OUT2, OUT1, ]
#     - W1:   [ VIN-, VIN+, OUT_COM, OUT4, OUT3, OUT2, OUT1, ]
#     - W1J3: [ VIN-, VIN+, OUT_COM, OUT4, OUT3, OUT2, OUT1, ]
#   -
#     - W1J2: [ INP1, INP2, INP3, INP4, INP_COM, XTXD, XRXD, XGND, ]
#     - W1:   [ INP1, INP2, INP3, INP4, INP_COM, XTXD, XRXD, XGND, ]
#     - W1J3: [ INP1, INP2, INP3, INP4, INP_COM, XTXD, XRXD, XGND, ]

connections = [
  [
    dict( W1J1 =  [ 'VIN-', 'VIN+', 'OUT_COM', 'OUT4', 'OUT3', 'OUT2', 'OUT1', ] ),
    dict( W1   =  [ 'VIN-', 'VIN+', 'OUT_COM', 'OUT4', 'OUT3', 'OUT2', 'OUT1', ] ),
    dict( W1J3 =  [ 'VIN-', 'VIN+', 'OUT_COM', 'OUT4', 'OUT3', 'OUT2', 'OUT1', ] ),
  ],
  [
    dict( W1J2 = [ 'INP1', 'INP2', 'INP3', 'INP4', 'INP_COM', 'XTXD', 'XRXD', 'XGND', ] ),
    dict( W1   = [ 'INP1', 'INP2', 'INP3', 'INP4', 'INP_COM', 'XTXD', 'XRXD', 'XGND', ] ),
    dict( W1J3 = [ 'INP1', 'INP2', 'INP3', 'INP4', 'INP_COM', 'XTXD', 'XRXD', 'XGND', ] ),
  ]
]


mlist = { "title": "My title" }

clist = Group( 'connectors', w1j1, w1j2, w1j3 )
wlist = Group( 'cables', w1 )

hlist = {}
hlist.update(  mlist )
hlist.update(  clist.dict() )
hlist.update(  wlist.dict() )
hlist.update(  { 'connections' : connections } )
 
harness, png, svg = wireviz.wireviz.parse( \
    hlist, return_types=("harness", "png", "svg"))
print(harness)
Path("out/png.png").write_bytes(png)
Path("out/svg.svg").write_text(svg, encoding="utf-8")

# # print the the connectors
# for c in connectors:
#   print(f'\nConnector {c.name}')
#   print(f'----------------------------------------')
#   print(c)
# 
# # print the the cables
# for w in cables:
#   print(f'\nCable {w.name}')
#   print(f'----------------------------------------')
#   print(w)
