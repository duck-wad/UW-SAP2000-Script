import os

from generate_geometry import *
from model_classes import *
from sap_interface import *

if __name__ == "__main__":
    """-------------------------- DEFINE MODEL CONSTRAINTS AND SECTIONS --------------------------"""

    # sections
    stringer_top_section = "HSSS1x0.12"
    stringer_bottom_section = "HSST0.5x1x0.065"
    stringer_web_section = "HSSP0.375x0.049"
    stringer_web_vertical_section = "HSSS0.625x0.049"

    leg_section = "HSSS1.25x0.095"
    leg_web_section = "HSSP0.375x0.049"

    moment_section = "HSSS0.625x0.049"
    moment_web_section = "HSSP0.375x0.049"
    moment_vertical_web_section = "HSSS0.5x0.049"

    # bridge dimensions
    bridge_length = 200.0
    top_chord_elevation = 22.0
    bridge_width = 30.0

    # stringer properties
    stringer_segments = 5
    stringer_depth = 5.0
    stringer_web_divisions = 3
    stringer_web_offset = 1.5

    # leg properties
    leg_depth = 5.0
    leg_web_divisions = 2
    outer_offset = 5.0  # height difference between the inner and outer chord

    # moment frame properties
    moment_top_elevation = 17.0
    moment_depth = 4.0
    moment_web_divisions = 3
    moment_web_offset = 2.0
    """ -------------------------- GENERATE GEOMETRY NODES -------------------------- """

    # generate the list of nodes by calling functions defined in generate_geometry.py
    # nodes are in pairs for the start and end
    (
        south_stringer_top_chord_nodes,
        south_stringer_bottom_chord_nodes,
        south_stringer_web_nodes,
        south_stringer_vertical_web_nodes,
    ) = generate_stringer_nodes(
        bridge_length,
        stringer_segments,
        0.0,
        top_chord_elevation,
        stringer_depth,
        stringer_web_divisions,
        stringer_web_offset,
    )
    (
        north_stringer_top_chord_nodes,
        north_stringer_bottom_chord_nodes,
        north_stringer_web_nodes,
        north_stringer_vertical_web_nodes,
    ) = generate_stringer_nodes(
        bridge_length,
        stringer_segments,
        bridge_width,
        top_chord_elevation,
        stringer_depth,
        stringer_web_divisions,
        stringer_web_offset,
    )

    south_west_leg_nodes, south_west_leg_web_nodes = generate_legs(
        "west",
        0.0,
        0.0,
        top_chord_elevation,
        leg_depth,
        leg_web_divisions,
        outer_offset,
    )
    north_west_leg_nodes, north_west_leg_web_nodes = generate_legs(
        "west",
        0.0,
        bridge_width,
        top_chord_elevation,
        leg_depth,
        leg_web_divisions,
        outer_offset,
    )
    south_east_leg_nodes, south_east_leg_web_nodes = generate_legs(
        "east",
        bridge_length,
        0.0,
        top_chord_elevation,
        leg_depth,
        leg_web_divisions,
        outer_offset,
    )
    north_east_leg_nodes, north_east_leg_web_nodes = generate_legs(
        "east",
        bridge_length,
        bridge_width,
        top_chord_elevation,
        leg_depth,
        leg_web_divisions,
        outer_offset,
    )

    west_moment_chord_nodes, west_moment_web_nodes, west_moment_vertical_web_nodes = (
        generate_moment_frame(
            bridge_width,
            0.0,
            moment_top_elevation,
            moment_depth,
            moment_web_divisions,
            moment_web_offset,
        ))
    east_moment_chord_nodes, east_moment_web_nodes, east_moment_vertical_web_nodes = (
        generate_moment_frame(
            bridge_width,
            bridge_length,
            moment_top_elevation,
            moment_depth,
            moment_web_divisions,
            moment_web_offset,
        ))
    """ -------------------------- CREATE FRAME MEMBER OBJECTS -------------------------- """

    all_members = []

    # based on the node lists and material sections, create objects for each frame that store their location, section etc
    south_stringer_top_chord_members = create_members(
        "south stringer", south_stringer_top_chord_nodes, stringer_top_section)
    south_stringer_bottom_chord_members = create_members(
        "south stringer", south_stringer_bottom_chord_nodes,
        stringer_bottom_section)
    south_stringer_web_members = create_members("south stringer",
                                                south_stringer_web_nodes,
                                                stringer_web_section)
    south_stringer_vertical_web_members = create_members(
        "south stringer",
        south_stringer_vertical_web_nodes,
        stringer_web_vertical_section,
    )
    north_stringer_top_chord_members = create_members(
        "north stringer", north_stringer_top_chord_nodes, stringer_top_section)
    north_stringer_bottom_chord_members = create_members(
        "north stringer", north_stringer_bottom_chord_nodes,
        stringer_bottom_section)
    north_stringer_web_members = create_members("north stringer",
                                                north_stringer_web_nodes,
                                                stringer_web_section)
    north_stringer_vertical_web_members = create_members(
        "north stringer",
        north_stringer_vertical_web_nodes,
        stringer_web_vertical_section,
    )
    all_members += [
        south_stringer_top_chord_members,
        south_stringer_bottom_chord_members,
        south_stringer_web_members,
        south_stringer_vertical_web_members,
        north_stringer_top_chord_members,
        north_stringer_bottom_chord_members,
        north_stringer_web_members,
        north_stringer_vertical_web_members,
    ]

    south_west_leg_members = create_members("south west leg",
                                            south_west_leg_nodes, leg_section)
    south_west_leg_web_members = create_members("south west leg",
                                                south_west_leg_web_nodes,
                                                leg_web_section)
    north_west_leg_members = create_members("north west leg",
                                            north_west_leg_nodes, leg_section)
    north_west_leg_web_members = create_members("north west leg",
                                                north_west_leg_web_nodes,
                                                leg_web_section)
    south_east_leg_members = create_members("south east leg",
                                            south_east_leg_nodes, leg_section)
    south_east_leg_web_members = create_members("south east leg",
                                                south_east_leg_web_nodes,
                                                leg_web_section)
    north_east_leg_members = create_members("north east leg",
                                            north_east_leg_nodes, leg_section)
    north_east_leg_web_members = create_members("north east leg",
                                                north_east_leg_web_nodes,
                                                leg_web_section)
    all_members += [
        south_west_leg_members,
        south_west_leg_web_members,
        north_west_leg_members,
        north_west_leg_web_members,
        south_east_leg_members,
        south_east_leg_web_members,
        north_east_leg_members,
        north_east_leg_web_members,
    ]

    west_moment_chord_members = create_members("west moment frame",
                                               west_moment_chord_nodes,
                                               moment_section)
    west_moment_web_members = create_members("west moment frame",
                                             west_moment_web_nodes,
                                             moment_web_section)
    west_moment_vertical_web_members = create_members(
        "west moment frame", west_moment_vertical_web_nodes,
        moment_vertical_web_section)
    east_moment_chord_members = create_members("east moment frame",
                                               east_moment_chord_nodes,
                                               moment_section)
    east_moment_web_members = create_members("east moment frame",
                                             east_moment_web_nodes,
                                             moment_web_section)
    east_moment_vertical_web_members = create_members(
        "east moment frame", east_moment_vertical_web_nodes,
        moment_vertical_web_section)
    all_members += [
        west_moment_chord_members,
        west_moment_web_members,
        west_moment_vertical_web_members,
        east_moment_chord_members,
        east_moment_web_members,
        east_moment_vertical_web_members,
    ]
    """ -------------------------- INTERFACE WITH SAP2000 -------------------------- """

    # path to model
    root_path = os.getcwd()
    base_file_path = root_path + "/BASE.sdb"
    os.makedirs("./models", exist_ok=True)
    model_path = root_path + "/models.MODEL.sdb"

    sap_object = sap_open()

    sap_model = sap_initialize_model(base_file_path, sap_object)

    for members in all_members:

        sap_member_names = sap_create_members(sap_model, members)

        # sap_create_members returns the list of the 'names' generated by SAP to keep track of the frames in model
        # set the name field of each member dataclass to the corresponding sap frame name
        for index, member in enumerate(members):
            member.name = sap_member_names[index]
