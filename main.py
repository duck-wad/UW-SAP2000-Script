import os

from define_constraints import *
from generate_geometry import *
from load_properties import *
from define_model_classes import *
from create_members import *
from sap_interface import *


''' -------------------------- DEFINE MODEL CONSTRAINTS -------------------------- '''
# make calls to functions defined in define_constraints
# ex. length, width, height = return_envelope()


''' -------------------------- GENERATE GEOMETRY -------------------------- '''

# generate the list of nodes by calling functions defined in generate_geometry.py
# ex. stringer_nodes = generate_stringer()
stringer_nodes = generate_stringer(20, 5)
leg_nodes = []
print(stringer_nodes)

''' -------------------------- IMPORT MODEL PROPERTIES -------------------------- '''
# import the model properties
materials, sections = load_model_data()
# hardcoded example
steel_mat = MaterialProperty(name='A992Fy50', type=1, elastic_mod=29000., poisson=0.3, thermal_coeff=6.500E-06)
stringer_HSS = BoxProperty(name='1x1.75x0.065', material=steel_mat, depth=1.75, width=1.0,
                           flange_thickness=0.065, web_thickness=0.065, corner_radius=0.0)


''' -------------------------- CREATE FRAME MEMBER OBJECTS -------------------------- '''
# based on the node lists and material sections, create objects for each frame 
# somewhere need to define what section we want to assign to each frame
stringer_members = create_members('stringer', stringer_nodes, stringer_HSS)


exit()

''' -------------------------- INTERFACE WITH SAP2000 -------------------------- '''
# pass the list of frame members to functions defined in sap_interface to create in SAP
# other stuff needs to be done here not really sure haven't looked into it much

# path to model
API_path = 'C:\\Users\\Nick\\source\\repos\\SAP2000 API\\Frame Generation Script'
model_path = API_path + os.sep + 'TEST.sdb'
# flag to True to attach to exis1ting instance of program
# if this is set to true, runtime will prob be lot faster if u just keep sap open
attach_to_instance = True
# flag to True to specify path to specific version of sap
# false, newest installation
specify_path = False
program_path = ''

""" sap_model = initialize_model(API_path, attach_to_instance, specify_path, program_path) """