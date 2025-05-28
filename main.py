import os

from model_classes import *
from data_loader import *
from sap_interface import *

# path to model
API_path = 'C:\\Users\\Nick\\source\\repos\\SAP2000 API\\Frame Generation Script'
model_path = API_path + os.sep + 'TEST.sdb'
# flag to True to attach to exis1ting instance of program
# false, new instance is started
attach_to_instance = False
# flag to True to specify path to specific version of sap
# false, newest installation
specify_path = False
program_path = ''

sap_model = initialize_model(API_path, attach_to_instance, specify_path, program_path)

materials, sections, members, load_patterns = load_model_data()

print(members[0])
print(members[1])
print(members[2])
print(load_patterns)