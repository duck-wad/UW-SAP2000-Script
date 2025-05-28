import os
import sys
import comtypes.client

def initialize_model(API_path, attach_to_instance, specify_path, program_path):

    if not os.path.exists(API_path):
        try:
            os.makedirs(API_path)
        except OSError:
            pass
    
    # create API helper object
    helper = comtypes.client.CreateObject('SAP2000v1.Helper')
    helper = helper.QueryInterface(comtypes.gen.SAP2000v1.cHelper)

    if attach_to_instance:
        # attach to running instance of SAP2000
        try:
            sap_object = helper.GetObject("CSI.SAP2000.API.SapObject")
        except (OSError, comtypes.COMError):
            print("No running instance of program found or failed to attach")
            sys.exit(-1)
    else:
        if specify_path:
            try:
                sap_object = helper.CreateObject(program_path)
            except (OSError, comtypes.COMError):
                print("Cannot start new instance of program")
                sys.exit(-1)
        else:
            try:
                sap_object = helper.CreateObjectProgID("CSI.SAP2000.API.SapObject")
            except (OSError, comtypes.COMError):
                print("Cannot start new instance of program")
                sys.exit(-1)
        # start SAP2000 application
        sap_object.ApplicationStart()

    #create sap_model object
    sap_model = sap_object.SapModel

    # initialize model
    sap_model.InitializeNewModel()

    sap_model.File.NewBlank()

    return sap_model

def define_units(sap_model, units):
    pass

# loop through list of materials and create in SAP
def define_materials(sap_model, materials):
    pass

# loop through list of sections and create in SAP
def define_sections(sap_model, sections, modifiers):
    pass

# loop through list of load patterns and create in SAP
def define_load_patterns(sap_model, load_patterns):
    pass

# loop through list of members and create in SAP
# since loads are grouped in member objects, define loads here too
def define_members(sap_model, members):
    pass

def run_model(sap_model):
    pass

def get_results(sap_model):
    pass