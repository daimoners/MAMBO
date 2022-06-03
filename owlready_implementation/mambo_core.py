from owlready2 import *

onto = get_ontology("./owlready_implementation/mambo.owl")
list(onto.classes())

# Main class 
class Material(Thing):
    namespace = onto

# Structural characteristics
class Structure(Thing):
    namespace = onto

class MolecularAggregate(Structure):
    namespace = onto

class Crystal(Structure):
    namespace = onto

# Structural sub-units of general Structures
class StructuralEntity(Thing):
    namespace = onto

class Atom(StructuralEntity):
    namespace = onto

class Particle(StructuralEntity):
    namespace = onto

class StructuralUnit(StructuralEntity):
    namespace = onto

class MolecularSystem(StructuralEntity):
    namespace = onto

# Chemical/physical properties
class Property(Thing):
    namespace = onto

class ChemicalProperty(Property):
    namespace = onto

class ElectroMagneticProperty(Property):
    namespace = onto

class MechanicalProperty(Property):
    namespace = onto
    

## Computational experiments, results and procedures
class Calculation(Thing):
    namespace = onto

class ComputationalMethod(Thing):
    namespace = onto

class DFT(ComputationalMethod):
    namespace = onto

class MD(ComputationalMethod):
    namespace = onto

class KMC(ComputationalMethod):
    namespace = onto


## Empirical experiments, results and procedures
class Measurement(Thing):
    namespace = onto

class ExperimentalMethod(Thing):
    namespace = onto

class ElectricalMethod(ExperimentalMethod):
    namespace = onto

class TOF(ElectricalMethod):
    namespace = onto

class OpticalMethod(ExperimentalMethod):
    namespace = onto



# PROPERTIES

with onto:
    # Object properties
    class hasProperty(ObjectProperty):
        domain = [Material]
        range = [Property]
     
    class hasStructure(ObjectProperty):
        domain = [Material]
        range = [Structure]
     
    class hasStructuralEntity(ObjectProperty):
        domain = [Structure]
        range = [StructuralEntity]
     
    class isPartOfParticle(ObjectProperty):
        domain = [Atom]
        range = [Particle]
     
    class isPartOfStructuralUnit(ObjectProperty):
        domain = [Particle]
        range = [StructuralUnit]
    
    class isPartOfMolecularSystem(ObjectProperty):
        domain = [StructuralUnit]
        range = [MolecularSystem]
    
    class hasCompInput(ObjectProperty):
        domain = [Calculation] 
        range = [Structure, Property]
    
    class isComputedBy(ObjectProperty):
        domain = [Property, Structure]
        range = [Calculation]
        inverse_property = hasCompInput
    
    class hasComputationalMethod(ObjectProperty):
        domain = [Calculation]
        range = [ComputationalMethod]
    
    class hasExpInput(ObjectProperty):
        domain = [Measurement]
        range = [Property, Structure]
    
    class isMeasuredBy(ObjectProperty):
        domain = [Property, Structure]
        range = [Measurement]
        inverse_property = hasExpInput
    
    class hasExperimentalMethod(ObjectProperty):
        domain = [Measurement]
        range = [ExperimentalMethod]
    
    # Data properties
    class name(DataProperty):
        domain = [Material]
        range = [str]
    
    class spacegroup(DataProperty):
        domain = [Structure]
        range = [str]
    
    class lattice(DataProperty):
        domain = [Structure]
        range = [str]
    
    class composition(DataProperty):
        domain = [Structure]
        range = [str]

    class charge(DataProperty):
        domain = [StructuralEntity]
        range = [float]

    class coordinates(DataProperty):
        domain = [StructuralUnit, Particle]
        range = [float]
    
    class formula(DataProperty):
        domain = [StructuralUnit, MolecularSystem]
        range = [str]

    class ID(DataProperty):
        domain = [Calculation]
        range = [str]

    class log(DataProperty):
        domain = [Measurement]
        range = [str]

    class quaternion(DataProperty):
        domain = [MolecularSystem, StructuralUnit]
        range = [float]

    class rotation_matrix(DataProperty):
        domain = [StructuralUnit, MolecularSystem]
        range = [float]

    class symbol(DataProperty):
        domain = [Atom]
        range = [str]

    class value(DataProperty):
        domain = [Property]
        range = [float]

    


list(onto.classes())
list(onto.properties())

onto.save(file="./owlready_implementation/mambo-ready.owl", format="rdfxml")
