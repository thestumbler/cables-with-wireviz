import wireviz
from wireviz.DataClasses import \
  Options, Tweak, Image, AdditionalComponent, Connector, \
  Cable, Connection, MatePin, MateComponent
from wireviz.wv_colors import COLOR_CODES, Color, ColorMode, \
  Colors, ColorScheme

from common import *

    # 'gauge': '0.129 mm2',
    # 'show_equiv': True,
class CABLE_ADM2704_26(Cable):
  kind = 'cable'
  defaults = {
    'gauge': "26 AWG",
    'color_code': 'DIN',
    'category': 'bundle',
    'notes': 'AWM 2704, 60C, 30VAC, Cable flame',
  }
  def __init__(self, name, *args, **kw):
   # , pins = None, pinlabels=None, pincolors=None):
    super().__init__( name, **{ **__class__.defaults, **kw } )
  def dict(self): return wvdict(self)


'''
cables:
  W1:
    <<: *template_awm2704_26awg
    length: 2
    wirecount: 16
    colors: [ 
      GNBK, WH,
      GN, BU, VT, GY, YE, 
      WHBK, OG, BUWH, RDWH, YEBK, 
      BN, BK, RD, 
      OGBK, GYBK, VTBK,
    ]
    wirelabels: [ 
      VIN-, VIN+, 
      OUT_COM, OUT4, OUT3, OUT2, OUT1, 
      INP1, INP2, INP3, INP4, INP_COM, 
      XTXD, XRXD, XGND,
   ]

'''





'''
@dataclass
class Cable:
    name: Designator
    bgcolor: Optional[Color] = None
    bgcolor_title: Optional[Color] = None
    manufacturer: Union[MultilineHypertext, List[MultilineHypertext], None] = None
    mpn: Union[MultilineHypertext, List[MultilineHypertext], None] = None
    supplier: Union[MultilineHypertext, List[MultilineHypertext], None] = None
    spn: Union[MultilineHypertext, List[MultilineHypertext], None] = None
    pn: Union[Hypertext, List[Hypertext], None] = None
    category: Optional[str] = None
    type: Optional[MultilineHypertext] = None
    gauge: Optional[float] = None
    gauge_unit: Optional[str] = None
    show_equiv: bool = False
    length: float = 0
    length_unit: Optional[str] = None
    color: Optional[Color] = None
    wirecount: Optional[int] = None
    shield: Union[bool, Color] = False
    image: Optional[Image] = None
    notes: Optional[MultilineHypertext] = None
    colors: List[Colors] = field(default_factory=list)
    wirelabels: List[Wire] = field(default_factory=list)
    color_code: Optional[ColorScheme] = None
    show_name: Optional[bool] = None
    show_wirecount: bool = True
    show_wirenumbers: Optional[bool] = None
    ignore_in_bom: bool = False
    additional_components: List[AdditionalComponent] = field(default_factory=list)
'''

