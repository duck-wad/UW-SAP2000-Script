from dataclasses import dataclass
from typing import Tuple, Optional, List
''' ------------------------- DATA CLASSES ------------------------- '''


@dataclass
class FrameMember:
    group: str  # identifier to denote what type of member this frame is part of ex) "south west leg"
    start: Tuple[float, float, float]  # (x, y, z) coordinate
    end: Tuple[float, float, float]  # (x, y, z) coordinate
    section: str  # string section property name
    coordinate_system: str  # ex. 'Global'

    # optional fields can be set after initialization
    id: Optional[
        str] = None  # this is the id that is returned by the SAP API when the frame is created
    start_restraint: Optional[Tuple[bool, bool, bool, bool, bool,
                                    bool]] = None  # 6DOF restraint
    end_restraint: Optional[Tuple[bool, bool, bool, bool, bool,
                                  bool]] = None  # 6DOF restraint
    start_release: Optional[Tuple[bool, bool, bool, bool, bool, bool]] = None
    end_release: Optional[Tuple[bool, bool, bool, bool, bool, bool]] = None
    distributed_loads: Optional[List["DistributedLoad"]] = None


@dataclass
class LoadPattern:
    name: str
    type: int  # see LoadType in model_enums
    self_weight: int
    add_load_case: bool  # if true, linear static load case is added


@dataclass
class DistributedLoad:
    load_case: str  # should verify if this load case exists when instantiating
    load_type: int  # 1 for force per length, 2 for moment per length
    load_direction: int  # 10 for gravity, 5 for global Y (lateral load case)
    dist_1: float  # distance from end I (first point) of frame
    dist_2: float  # distance from end J (second point) of frame
    val_1: float
    val_2: float
    coordinate_system: Optional[str] = None


''' ------------------------- FUNCTIONS TO INSTANTIATE OBJECTS ------------------------- '''


# create the initial geometry of the members
def create_members(group, node_pairs, section, coordinate_system='Global'):

    member_list = []

    for node_pair in node_pairs:
        # pass in args as dictionary to FrameMember() to dynamically check for restraints/releases=None
        args = {
            'group': group,
            'start': node_pair[0],
            'end': node_pair[1],
            'section': section,
            'coordinate_system': coordinate_system
        }

        # ** unpack list of arguments
        member_list.append(FrameMember(**args))

    return member_list
