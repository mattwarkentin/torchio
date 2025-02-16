from .fpg import FPG
from .bite import BITE3
from .slicer import Slicer
from .episurg import EPISURG
from .ixi import IXI, IXITiny
from .rsna_miccai import RSNAMICCAI
from .itk_snap import BrainTumor, T1T2, AorticValve
from .visible_human import VisibleFemale, VisibleMale
from .mni import Colin27, Sheep, Pediatric, ICBM2009CNonlinearSymmetric


__all__ = [
    'FPG',
    'Slicer',
    'BITE3',
    'IXI',
    'IXITiny',
    'RSNAMICCAI',
    'EPISURG',
    'BrainTumor',
    'T1T2',
    'AorticValve',
    'Colin27',
    'Sheep',
    'Pediatric',
    'ICBM2009CNonlinearSymmetric',
    'VisibleFemale',
    'VisibleMale',
]
