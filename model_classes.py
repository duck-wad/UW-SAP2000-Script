from enum import IntEnum
from dataclasses import dataclass, field
from typing import Tuple, Optional, List


''' ------------------------- ENUMS ------------------------- '''


class MaterialType(IntEnum):
    STEEL = 1
    CONCRETE = 2
    NODESIGN = 3
    ALUMINUM = 4
    COLDFORM = 5
    REBAR = 6
    TENDON = 7

class LoadType(IntEnum):
    LTYPE_DEAD = 1
    LTYPE_SUPERDEAD = 2
    LTYPE_LIVE = 3
    LTYPE_REDUCELIVE = 4
    LTYPE_QUAKE = 5
    LTYPE_WIND= 6
    LTYPE_SNOW = 7
    LTYPE_OTHER = 8
    LTYPE_MOVE = 9
    LTYPE_TEMPERATURE = 10
    LTYPE_ROOFLIVE = 11
    LTYPE_NOTIONAL = 12
    LTYPE_PATTERNLIVE = 13
    LTYPE_WAVE= 14
    LTYPE_BRAKING = 15
    LTYPE_CENTRIFUGAL = 16
    LTYPE_FRICTION = 17
    LTYPE_ICE = 18
    LTYPE_WINDONLIVELOAD = 19
    LTYPE_HORIZONTALEARTHPRESSURE = 20
    LTYPE_VERTICALEARTHPRESSURE = 21
    LTYPE_EARTHSURCHARGE = 22
    LTYPE_DOWNDRAG = 23
    LTYPE_VEHICLECOLLISION = 24
    LTYPE_VESSELCOLLISION = 25
    LTYPE_TEMPERATUREGRADIENT = 26
    LTYPE_SETTLEMENT = 27
    LTYPE_SHRINKAGE = 28
    LTYPE_CREEP = 29
    LTYPE_WATERLOADPRESSURE = 30
    LTYPE_LIVELOADSURCHARGE = 31
    LTYPE_LOCKEDINFORCES = 32
    LTYPE_PEDESTRIANLL = 33
    LTYPE_PRESTRESS = 34
    LTYPE_HYPERSTATIC = 35
    LTYPE_BOUYANCY = 36
    LTYPE_STREAMFLOW = 37
    LTYPE_IMPACT = 38
    LTYPE_CONSTRUCTION = 39

class DistributedLoadType(IntEnum):
    FORCE_PER_LENGTH = 1
    MOMENT_PER_LENGTH = 2

class LoadDirection(IntEnum):
    # local1-3 only apply when coordinate system is set to local
    LOCAL_1 = 1
    LOCAL_2 = 2
    LOCAL_3 = 3
    GLOBAL_X = 4
    GLOBAL_Y = 5
    GLOBAL_Z = 6
    PROJECTED_X = 7
    PROJECTED_Y = 8
    PROJECTED_Z = 9
    GRAVITY = 10
    PROJECTED_GRAVITY = 11

class PointLoadLocation(IntEnum):
    START = 0
    END = 1


''' ------------------------- DATA CLASSES ------------------------- '''


@dataclass
class MaterialProperty:
    name: str 
    type: MaterialType # 1=steel, 2=concrete, 3=nodesign, 4=aluminum, 5=coldform, 6=rebar, 7=tendon
    elastic_mod: float
    poisson: float
    thermal_coeff: float

@dataclass
class SectionProperty:
    name: str
    material: str
    depth: float 
    width: float

@dataclass
class FrameMember:
    name: str
    start: Tuple[float, float, float]  # (x, y, z) coordinate
    end: Tuple[float, float, float]    # (x, y, z) coordinate
    section: str # string section property name
    coordinate_system: str
    start_restraint: Optional[Tuple[bool, bool, bool, bool, bool, bool]] = None # 6DOF restraint
    end_restraint: Optional[Tuple[bool, bool, bool, bool, bool, bool]] = None # 6DOF restraint
    point_loads: List["PointLoad"] = field(default_factory=list)
    distributed_loads: List["DistributedLoad"] = field(default_factory=list)

    # enforce expected structure
    def __post_init__(self):
        if len(self.start) != 3:
            raise ValueError(f"'start' must be a 3-tuple")
        if len(self.end) != 3:
            raise ValueError(f"'end' must be a 3-tuple")
        if (self.start_restraint != None) and (len(self.start_restraint) != 6) :
            raise ValueError(f"'start_restraint' must be a 6-tuple")
        if (self.end_restraint != None) and (len(self.end_restraint) != 6):
            raise ValueError(f"end_restraint must be a 6-tuple")

@dataclass 
class LoadPattern:
    name: str
    type: LoadType # see LoadType
    self_weight: int 
    add_load_case: bool # if true, linear static load case is added

@dataclass
class PointLoad:
    location: PointLoadLocation # either start or end
    load_case: str # should verify if this load case exists when instantiating
    load_value: Tuple[float, float, float, float, float, float] # xyz force, xyz moment

    def __point__init__(self):
        if len(self.load_value) != 6:
            raise ValueError(f"'load_value' must be a 6-tuple")

@dataclass
class DistributedLoad:
    load_case: str # should verify if this load case exists when instantiating
    load_type: DistributedLoadType
    load_direction: LoadDirection
    dist_1: float # distance from end I (first point) of frame 
    dist_2: float # distance from end J (second point) of frame
    val_1: float
    val_2: float 
    coordinate_system: Optional[str] = None

