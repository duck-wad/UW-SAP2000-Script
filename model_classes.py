from dataclasses import dataclass
from typing import Tuple, Optional, List

""" ------------------------- DATA CLASSES ------------------------- """


@dataclass
class FrameMember:
    start: Tuple[float, float, float]  # (x, y, z) coordinate
    end: Tuple[float, float, float]  # (x, y, z) coordinate
    section: str  # string section property name
    coordinate_system: str  # ex. 'Global'

    # optional fields can be set after initialization
    flag: Optional[str] = (
        None  # to check shit idk. mainly to check if the member is top stringer
    )
    id: Optional[str] = (
        None  # this is the id that is returned by the SAP API when the frame is created
    )
    start_restraint: Optional[Tuple[bool, bool, bool, bool, bool, bool]] = (
        None  # 6DOF restraint
    )
    end_restraint: Optional[Tuple[bool, bool, bool, bool, bool, bool]] = (
        None  # 6DOF restraint
    )
    start_release: Optional[Tuple[bool, bool, bool, bool, bool, bool]] = None
    end_release: Optional[Tuple[bool, bool, bool, bool, bool, bool]] = None
    # list of lists in case a single frame is subject to both L1 and L2 for a single load case
    distributed_loads: Optional[List[List["DistributedLoad"]]] = None


@dataclass
class DistributedLoad:
    load_pattern: str
    load_type: int  # 1 for force per length, 2 for moment per length
    load_direction: int  # 10 for gravity, 5 for global Y (lateral load case)
    dist_1: float  # distance from end I (first point) of frame
    dist_2: float  # distance from end J (second point) of frame
    val_1: float
    val_2: float
    coordinate_system: Optional[str] = None


""" ------------------------- FUNCTIONS TO MANIPULATE DATA CLASSES ------------------------- """


# create the initial geometry of the members
def create_members(node_pairs, section, coordinate_system="Global", flag=None):

    member_list = []

    for node_pair in node_pairs:
        # pass in args as dictionary to FrameMember() to dynamically check for restraints/releases=None
        args = {
            "start": node_pair[0],
            "end": node_pair[1],
            "section": section,
            "coordinate_system": coordinate_system,
            "flag": flag,
        }

        # for the west side legs set pins, for the east side set rollers
        if flag == "west leg":
            if node_pair[0][2] < node_pair[1][2]:
                args["start_restraint"] = (True, True, True, False, False, False)
            else:
                args["end_restraint"] = (True, True, True, False, False, False)
        if flag == "east leg":
            if node_pair[0][2] < node_pair[1][2]:
                args["start_restraint"] = (False, False, True, False, False, False)
            else:
                args["end_restraint"] = (False, False, True, False, False, False)

        # ** unpack list of arguments
        member_list.append(FrameMember(**args))

    return member_list
