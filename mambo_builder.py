from owlready2 import *

onto = get_ontology("./mambo_ready.owl")


with onto:
    # Main class 
    class Material(Thing):
        pass
    
    # Structural characteristics
    class Structure(Thing):
        pass
    
    class MolecularAggregate(Thing):
        pass
    
    class Crystal(Thing):
        pass
    
    # Structural sub-units of general Structures
    class Atom(Thing):
        pass
    
    class Particle(Thing):
        pass
    
    class StructuralUnit(Thing):
        pass
    
    class MolecularSystem(Thing):
        pass
    
    # Chemical/physical properties
    class Property(Thing):
        pass
    
    class ChemicalProperty(Property):
        pass
        
    class ElectroMagneticProperty(Property):
        pass
    
    class MechanicalProperty(Property):
        pass
        
    
    ## Computational experiments, results and procedures
    class Calculation(Thing):
        pass
    
    class ComputationalMethod(Thing):
        pass
    
    class DFT(ComputationalMethod):
        pass
    
    class MD(ComputationalMethod):
        pass
    
    class KMC(ComputationalMethod):
        pass
    
    
    ## Empirical experiments, results and procedures
    class Measurement(Thing):
        pass
    
    class ExperimentalMethod(Thing):
        pass
    
    class ElectricalMethod(ExperimentalMethod):
        pass
    
    class TOF(ElectricalMethod):
        pass
    
    class OpticalMethod(ExperimentalMethod):
        pass
    
    # PROPERTIES
    
    # Object properties
    class hasProperty(ObjectProperty):
        domain = [Material]
        range = [Property]
     
    class hasStructure(ObjectProperty):
        domain = [Material]
        range = [Structure]
     
    class hasAtom(ObjectProperty):
        domain = [Structure]
        range = [Atom]
     
    class hasParticle(ObjectProperty):
        domain = [Structure]
        range = [Particle]
     
    class hasStructuralUnit(ObjectProperty):
        domain = [Structure]
        range = [StructuralUnit]
     
    class hasMolecularSystem(ObjectProperty):
        domain = [Structure]
        range = [MolecularSystem]
     
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
        domain = [Atom, Particle, StructuralUnit, MolecularSystem]
        range = [float]
    
    class coordinates(DataProperty):
        domain = [StructuralUnit, Particle]
        range = [float]
    
    class formula(DataProperty, FunctionalProperty):
        domain = [StructuralUnit, MolecularSystem, Particle]
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
    
    class symbol(DataProperty, FunctionalProperty):
        domain = [Atom]
        range = [str]
    
    class value(DataProperty):
        domain = [Property]
        range = [float]
    
    class unit(DataProperty, FunctionalProperty):
        domain = [Property]
        range = [str]
    
    class atomic_number(DataProperty):
        domain = [Atom]
        range = [int]

    class atoms(DataProperty):
        domain = [Structure]
        range = [str]

    class molecules(DataProperty):
        domain = [Structure]
        range = [str]

# Instances
#particle1 = onto.Particle("WaterHydrogens")
#onto.WaterHydrogens.formula = "H2"
#onto.WaterHydrogens.coordinates = [1.0,1.0,1.0]
#particle1.isPartOfStructuralUnit = []
#atom1 = onto.Atom("Hydrogen")
#atom1.isPartOfParticle.append(particle1)
#atom1.symbol = "H"
##
#print(atom1)
##
#sync_reasoner()
    


onto.save(file="./mambo_ready.owl", format="rdfxml")
