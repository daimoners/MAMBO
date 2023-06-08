import os
import sys
from owlready2 import *

mambo_ready = get_ontology("mambo_ready.owl")

# BUILD PHASE
if "core" in sys.argv:
    mambo_core = os.listdir("./src/core")
    for core_element in mambo_core:
        if core_element not in ["object_properties.py", "data_properties.py"]:
            exec(open("./src/core/"+core_element).read())
    exec(open("./src/core/object_properties.py").read())
    exec(open("./src/core/data_properties.py").read())

if "modules" in sys.argv:
    mambo_modules = os.listdir("./src/modules")
    for module in mambo_modules:
        exec(open("./src/modules/"+module).read())


# TEST PHASE
# for cl in mambo_ready.classes():
#     print(cl)

# for dp in mambo_ready.object_properties():
#     print(dp)


# SAVE ONTOLOGY
mambo_ready.save(file="./mambo_ready.owl")

os.system("python src/inspect_mambo.py mambo_ready.owl")
