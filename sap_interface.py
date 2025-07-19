import os
import sys
import comtypes.client


def sap_open():
    # create API helper object
    helper = comtypes.client.CreateObject('SAP2000v1.Helper')
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
        sap_members.append(
            sap_model.FrameObj.AddByCoord(*member.start, *member.end, 'foo',
                                          member.section)[0])

    return sap_members


# loop through list of load patterns and create in SAP
def sap_load_patterns(sap_model, load_patterns):
    pass


def sap_run_model(sap_model):
    pass


def sap_get_results(sap_model):
    pass
