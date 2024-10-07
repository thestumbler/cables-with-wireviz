from dataclasses import dataclass
import wireviz
from wireviz.DataClasses import \
  Options, Tweak, Image, AdditionalComponent, Connector, \
  Cable, Connection, MatePin, MateComponent

from utils import *


@connectorclass
@dataclass
class CPC16F(Connector):
  defaults = {
    'type' : 'CPC Series Chassis Mount',
    'subtype' :  'female',
    'hide_disconnected_pins' :  False,
    'pincount' :  16,
    'notes' :  'Digikey A1305-ND',
    'mpn' :  '206036-1',
    'manufacturer' :  'TE Connectivity',
    'image' : Image( src = 'images/cpc-16pin-360px.png'),
  }

@connectorclass
@dataclass
class MTA_100_09(Connector):
  defaults = {
    'type'         : 'MTA-100 IDC',
    'subtype'      : 'female',
    'hide_disconnected_pins' :  True,
    'pincount'     : 9,
    'notes'        : 'Digikey A124524-ND',
    'mpn'          : 'TE 3-643814-9',
    'manufacturer' : 'TE Connectivity',
    'image'        : Image( src = 'images/mta100-9-360px.png', )
  }

@connectorclass
@dataclass
class MTA_100_09_male(Connector):
  defaults = {
    'type'         : 'MTA-100 IDC FLYING',
    'subtype'      : 'male',
    'hide_disconnected_pins' :  True,
    'pincount'     : 9,
    'notes'        : 'Newark 96Y3544',
    'mpn'          : 'TE 647000-9',
    'manufacturer' : 'TE Connectivity',
    'image'        : Image(src = 'images/mta100-9-male-360px.png'),
  }

@connectorclass
@dataclass
class PICOBLADE_7S(Connector):
  defaults = {
    'type': 'PICOBLADE 7-POSN SOCKET',
    'subtype': 'female',
    'pincount': 7,
    'hide_disconnected_pins': True,
    'notes': 'Digikey WM1725-ND',
    'mpn': 'Molex 0510210700',
    'manufacturer': 'Molex',
    'image': Image(src = 'images/picoblade-51021-07-socket.png' ),
    #'image': 'images/picoblade-51021-07-socket.png',
  }

# TBD
#    additional_components:
#      -
#        type: Crimp Socket, Molex 50079-8x00
#        qty_multiplier: populated # multipier for quantity (number of populated pins)
#        manufacturer: Molex # set manufacter name
#        mpn: 0500798x00

@connectorclass
@dataclass
class PICOBLADE_8S(Connector):
  defaults = {
    'type': 'PICOBLADE 8-POSN SOCKET',
    'subtype': 'female',
    'pincount': 8,
    'hide_disconnected_pins': True,
    'notes': 'Digikey WM1726-ND',
    'mpn': 'Molex 0510210700',
    'manufacturer': 'Molex',
    'image': Image(src = 'images/picoblade-51021-07-socket.png' ),
  }

@connectorclass
@dataclass
class JST_SMR_18S(Connector):
  defaults = {
    'type': 'JST 18-POSN SOCKET',
    'subtype': 'female',
    'pincount': 18,
    'hide_disconnected_pins': False,
    'notes': 'TBD',
    'mpn': 'SMR-18V-N',
    'manufacturer': 'JST',
    'image': Image(src = 'images/jst-smr-18.png'),
  }


'''
  - &template_mta_100_8
    type: MTA-100 IDC
    subtype: female
    pincount: 8
    hide_disconnected_pins: True
    notes: Digikey A34823-ND
    mpn: TE 3-641534-8
    manufacturer: TE Connectivity
    image:
      src: images/mta100-8-360px.png

  - &template_mta_100_4
    type: MTA-100 IDC
    subtype: female
    pincount: 4
    hide_disconnected_pins: True
    notes: Digikey A30980-ND
    mpn: TE 3-640441-4
    manufacturer: TE Connectivity
    image:
      src: images/mta100-4-360px.png

  - &template_mta_100_3
    type: MTA-100 IDC
    subtype: female
    pincount: 3
    hide_disconnected_pins: True
    notes: Digikey A30979-ND
    mpn: TE 3-640441-3
    manufacturer: TE Connectivity
    image:
      src: images/mta100-3-360px.png

  - &template_mta_100_2
    type: MTA-100 IDC
    subtype: female
    pincount: 2
    hide_disconnected_pins: True
    notes: Digikey A30978-ND
    mpn: TE 3-640441-2
    manufacturer: TE Connectivity
    image:
      src: images/mta100-2-360px.png

  - &template_eurostyle_molex_ese_39510_12p
    type: EUROSTYLE ESE 12-POSN PLUG
    subtype: male
    pincount: 12
    hide_disconnected_pins: True
    notes: Digikey WM25587-ND
    mpn: 0395105012
    manufacturer: Molex
    image:
      src: images/molex-eurostyle-ese-39510-12.png

  - &template_eurostyle_molex_ese_39510_03p
    type: EUROSTYLE ESE 3-POSN PLUG
    subtype: male
    pincount: 3
    hide_disconnected_pins: True
    notes: Digikey WM20083-ND
    mpn: 0395105003
    manufacturer: Molex
    image:
      src: images/molex-eurostyle-ese-39510-03.png

  - &template_picoblade_6s
    type: PICOBLADE 6-POSN SOCKET
    subtype: female
    pincount: 6
    hide_disconnected_pins: True
    notes: Digikey WM1724-ND
    mpn: Molex 0510210600
    manufacturer: Molex
    image:
      src: images/picoblade-51021-06-socket.png

  - &template_picoblade_7s
    type: PICOBLADE 7-POSN SOCKET
    subtype: female
    pincount: 7
    hide_disconnected_pins: True
    notes: Digikey WM1725-ND
    mpn: Molex 0510210700
    manufacturer: Molex
    image:
      src: images/picoblade-51021-07-socket.png
    additional_components:
      -
        type: Crimp Socket, Molex 50079-8x00
        qty_multiplier: populated # multipier for quantity (number of populated pins)
        manufacturer: Molex # set manufacter name
        mpn: 0500798x00

  - &template_picoblade_8s
    type: PICOBLADE 8-POSN SOCKET
    subtype: female
    pincount: 8
    hide_disconnected_pins: True
    notes: Digikey WM1726-ND
    mpn: Molex 0510210800
    manufacturer: Molex
    image:
      src: images/picoblade-51021-08-socket.png
    additional_components:
      -
        type: Crimp Socket, Molex 50079-8x00
        qty_multiplier: populated # multipier for quantity (number of populated pins)
        manufacturer: Molex # set manufacter name
        mpn: 0500798x00


  - &template_jst_smr_18s
    type: JST 18-POSN SOCKET
    subtype: female
    pincount: 18
    hide_disconnected_pins: False
    notes: TBD
    mpn: SMR-18V-N
    manufacturer: JST
    image:
      src: images/jst-smr-18.png
    additional_components:
      -
        type: Crimp Socket Pin SHF-001T-0.8BS 
        qty_multiplier: populated # multipier for quantity (number of populated pins)
        manufacturer: JST # set manufacter name
        mpn: SHF-001T-0.8BS 

  - &template_bare_wire
    style: simple
    type: Bare wire
    show_name: False
    pincount: 1

  - &template_ferrule_pwr_pic
    image:
      src: images/ferrule-240px.png

  - &template_ferrule_pwr
    style: simple
    type: Crimp ferrule
    subtype: 0.75 mm2
    pincount: 1

  - &template_hookup_wire_signal
    gauge: 22 AWG 
    show_equiv: True
    color_code: DIN
    category: bundle
    mpn: 6823 
    manufacturer: Alpha Wire
    notes: EU Low Voltage 2006/95/EC, stranded (7/30)

  - &template_hookup_wire_power
    gauge: 20 AWG
    show_equiv: True
    color_code: DIN
    category: bundle
    mpn: 7123 
    manufacturer: Alpha Wire
    notes: UL Style 1430 300V @ 105C, stranded (7/28)

  - &template_avvr_signal_16_0p12
    gauge: 0.12 mm2
    show_equiv: True
    color_code: DIN
    category: bundle
    mpn: 6823 
    manufacturer: Alpha Wire
    notes: EU Low Voltage 2006/95/EC, stranded (7/30)

  - &template_awm2704_26awg
    gauge: 26 AWG
    # gauge: 0.129 mm2
    # show_equiv: True
    color_code: DIN
    category: bundle
    notes: AWM 2704, 60C, 30VAC, Cable flame
'''



