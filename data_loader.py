import pandas as pd
from model_classes import *

# read in materials, member properties, etc from excel
# right now just hardcode

def load_materials():
    materials = [
        MaterialProperty('CONC', MaterialType.CONCRETE, 3600, 0.2, 0.0000055)
    ]
    return materials

def load_sections():
    sections = [
        SectionProperty('R1', 'CONC', 12, 12)
    ]
    return sections

def load_load_patterns():
    load_patterns = [
        LoadPattern('1', LoadType.LTYPE_OTHER, 1, True),
        LoadPattern('2', LoadType.LTYPE_OTHER, 0, True),
        LoadPattern('3', LoadType.LTYPE_OTHER, 0, True),
    ]
    return load_patterns

def load_members():
    members = [
        FrameMember('1', (0,0,0), (0, 0, 10), 'R1', 'Global'),
        FrameMember('2', (0, 0, 10), (8, 0, 16), 'R1', 'Global'),
        FrameMember('3', (-4, 0, 10), (0, 0, 10), 'R1', 'Global')
    ]

    # loads are hard coded for now
    members[2].point_loads.append(PointLoad(PointLoadLocation.START, '2', (0, 0, -10, 0, 0, 0)))
    members[2].distributed_loads.append(DistributedLoad('2', DistributedLoadType.FORCE_PER_LENGTH,
                                                        LoadDirection.GRAVITY, 0, 1, 1.8, 1.8))
    members[2].point_loads.append(PointLoad(PointLoadLocation.END, '3', (0,0,-17.2,0,-54.4,0)))

    return members

def load_model_data():
    materials = load_materials()
    sections = load_sections()
    members = load_members()
    load_patterns = load_load_patterns()
    return materials, sections, members, load_patterns