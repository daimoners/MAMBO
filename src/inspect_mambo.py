import os
import sys
from owlready2 import *

onto_file = sys.argv[1]
# mambo_ready = get_ontology("mambo_ready.owl").load()
onto = get_ontology(onto_file).load()

# mambo_core = os.listdir("./src/core/")
# mambo_modules = os.listdir("./src/modules/")



# TEST PHASE
print("Classes: ")
for cl in onto.classes():
    print(cl)

print("Object properties: ")
for obj in onto.object_properties():
    print(obj)
    
print("Data properties: ")
for data in onto.data_properties():
    print(data)

