from define_model_classes import FrameMember

# create the frame member objects defined in define_model_classes based on geometry from generate_geometry
# return a list of frame member objects 

# restraints should have same shape as nodes?
def create_members(name, nodes, section, coordinate_system='Global', restraints=None, releases=None):
    member_list = []

    if restraints is not None and len(restraints) != len(nodes):
        raise ValueError("Restraints should be same length as number of nodes")
    if releases is not None and len(restraints) != len(nodes):
        raise ValueError("Releases should be same length as number of nodes")
    for i in range(len(nodes)-1):         
        # pass in args as dictionary to FrameMember() to dynamically check for restraints/releases=None  
        args = {
            'name': name, 
            'start': nodes[i],
            'end': nodes[i+1],
            'section': section,
            'coordinate_system': coordinate_system
        }
        if restraints is not None:
            args['start_restraint'] = restraints[i]
            args['end_restraint'] = restraints[i+1]
        if releases is not None:
            args['start_release'] = releases[i]
            args['end_release'] = releases[i+1]
        
        # ** unpack list of arguments
        member_list.append(FrameMember(**args))

    return member_list
