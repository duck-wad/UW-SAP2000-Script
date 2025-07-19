import os
import sys
import comtypes.client


def sap_open():
    # create API helper object
    helper = comtypes.client.CreateObject("SAP2000v1.Helper")
    helper = helper.QueryInterface(comtypes.gen.SAP2000v1.cHelper)
    sap_object = helper.GetObject("CSI.SAP2000.API.SapObject")
    if sap_object is None:
        sap_object = helper.CreateObjectProgID("CSI.SAP2000.API.SapObject")
        sap_object.ApplicationStart()

    return sap_object


def sap_close(sap_object):
    ret = sap_object.ApplicationExit(False)
    sap_object = None


def sap_initialize_model(base_file_path, sap_object):

    sap_model = sap_object.SapModel
    ret = sap_model.File.OpenFile(base_file_path)
    return sap_model


# loop through list of members and create in SAP
# since loads are grouped in member objects, define loads here too
def sap_create_members(sap_model, members):
    sap_members = []

    for member in members:
        name = sap_model.FrameObj.AddByCoord(
            *member.start, *member.end, "foo", member.section
        )[0]
        sap_members.append(name)

        start_point = ""
        end_point = ""
        start_point, end_point, ret = sap_model.FrameObj.GetPoints(
            name, start_point, end_point
        )

        if member.start_restraint != None:
            ret = sap_model.PointObj.SetRestraint(start_point, member.start_restraint)
        if member.end_restraint != None:
            ret = sap_model.PointObj.SetRestraint(end_point, member.end_restraint)

    return sap_members


# separate function to create the stringer
# create initially as one single stringer member, apply the distributed loads,
# and then subdivide into individual frames based on the start and end coordinates of each frame
def sap_create_stringer(sap_model, members, vertical_loads, L1_value, L2_value):
    starting_point = members[0].start
    ending_point = members[-1].end
    stringer_length = ending_point[0] - starting_point[0]

    frame, ret = sap_model.FrameObj.AddByCoord(
        *starting_point, *ending_point, "foo", members[0].section
    )
    for load in vertical_loads:
        L1_start_relative = load["L1"][0] / stringer_length
        L1_end_relative = load["L1"][1] / stringer_length
        L2_start_relative = load["L2"][0] / stringer_length
        L2_end_relative = load["L2"][1] / stringer_length
        ret = sap_model.FrameObj.SetLoadDistributed(
            frame,
            load["Name"],
            1,
            10,
            L1_start_relative,
            L1_end_relative,
            L1_value,
            L1_value,
            Replace=False,
        )
        ret = sap_model.FrameObj.SetLoadDistributed(
            frame,
            load["Name"],
            1,
            10,
            L2_start_relative,
            L2_end_relative,
            L2_value,
            L2_value,
            Replace=False,
        )
    for member in members:
        ret = sap_model.PointObj.AddCartesian(*member.end)

    # select all objects in the model and divide at the intersections with joints
    # to split stringer into individual frames
    ret = sap_model.SelectObj.All()
    _, stringer_frames, ret = sap_model.EditFrame.DivideAtIntersections(frame, 0, [])

    return stringer_frames


# loop through list of load patterns and create in SAP
def sap_add_load_patterns(sap_model, vertical_loads, lateral_loads):
    # case name, type, self weight multiplier, add linear static load case
    ret = sap_model.LoadPatterns.Add("DEAD", 1, 1, True)
    for load in vertical_loads:
        ret = sap_model.LoadPatterns.Add(load["Name"], 8, 0, True)
    for load in lateral_loads:
        ret = sap_model.LoadPatterns.Add(load["Name"], 8, 0, True)


def sap_run_model(sap_model):
    pass


def sap_get_results(sap_model):
    pass
