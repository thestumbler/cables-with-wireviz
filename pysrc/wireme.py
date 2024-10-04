#!/usr/bin/env python

import wireviz
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


connectors = [ w1j1, w1j2, w1j3, ]
cables = [ w1 ]

# print the the connectors
for c in connectors:
  print(f'\nConnector {c.name}')
  print(f'----------------------------------------')
  print(c)

# print the the cables
for w in cables:
  print(f'\nCable {w.name}')
  print(f'----------------------------------------')
  print(w)

# I'm lost at this point....

meta_dict = {
  "title": "My title",
}

'''
harness_dict = {
  "metadata": meta_dict,
  "connectors": connectors_dict,
  "cables": cables_dict,
  "connections": connections_list,
}

parse(harness_dict, ...)
'''

