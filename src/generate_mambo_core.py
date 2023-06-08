import os
import sys
from owlready2 import *

mambo_ready = get_ontology("mambo_ready.owl")

# BUILD PHASE
# CLASSES
class Material(Thing):
    namespace = mambo_ready

class Property(Thing):
    namespace = mambo_ready

class ChemicalProperty(Property):
    pass

class ElectroMagneticProperty(Property):
    pass

class MechanicalProperty(Property):
    pass

class Structure(Thing):
    namespace = mambo_ready

class Crystal(Structure):
    pass

class MolecularAggregate(Structure):
    pass


# STRUCTURAL ENTITY
class StructuralEntity(Thing):
    namespace = mambo_ready

class Atom(StructuralEntity):
    pass

class MolecularSystem(StructuralEntity):
    pass

class Particle(StructuralEntity):
    pass

class StructuralUnit(StructuralEntity):
    pass

class Experiment(Thing):
    namespace = mambo_ready

# TODO: check how to inherit from other ontologies (`continuant`, `continuant` `fiat boundary`, `process`)

# EXPERIMENTAL METHOD
class ExperimentalMethod(Thing):
    namespace = mambo_ready

class ElectricalMethod(ExperimentalMethod):
    pass

class TOF(ElectricalMethod):
    pass

class OpticalMethod(ExperimentalMethod):
    pass

class Simulation(Thing):
    namespace = mambo_ready



# COMPUTATIONAL METHOD
class ComputationalMethod(Thing):
    namespace = mambo_ready

# ALGORITHM
class Algorithm(Thing):
    namespace = mambo_ready

class MolecularDynamics(Algorithm):
    pass

class Optimizer(Algorithm):
    pass

class StructureManipulation(Algorithm):
    pass


# OBJECT PROPERTIES
# MATERIAL
class has_property(ObjectProperty):
    namespace = mambo_ready
    domain = [Material]
    range = [Property]

class has_structure(ObjectProperty):
    namespace = mambo_ready
    domain = [Material]
    range = [Structure]

# STRUCTURE
class has_structural_entity(ObjectProperty):
    namespace = mambo_ready
    domain = [Structure]
    range = [Atom, Particle, StructuralUnit, MolecularSystem, StructuralEntity]
    # inverse_property = is_structural_entity_of

class is_part_of(ObjectProperty):
    namespace = mambo_ready
    domain = [Atom, MolecularSystem, Particle, StructuralUnit]
    range = [MolecularAggregate, MolecularSystem, Particle, StructuralUnit]

class has_subunit(ObjectProperty):
    namespace = mambo_ready
    domain = [MolecularAggregate, MolecularSystem, Particle, StructuralUnit]
    range = [Atom, MolecularSystem, Particle, StructuralUnit]
    inverse_property = is_part_of

class is_structural_entity_of(ObjectProperty):
    namespace = mambo_ready
    domain = [Atom, Particle, StructuralUnit, MolecularSystem, StructuralEntity]
    range = [Structure]
    inverse_property = has_structural_entity

# SIMULATION
class has_computational_input(ObjectProperty):
    namespace = mambo_ready
    domain = [Simulation]
    range = [Property, Structure]

class has_computational_output(ObjectProperty):
    namespace = mambo_ready
    domain = [Simulation]
    range = [Property, Structure]

class is_computed_by(ObjectProperty):
    namespace = mambo_ready
    domain = [Property, Structure]
    range = [Simulation]
    inverse_property = has_computational_output

class use_computational_method(ObjectProperty):
    namespace = mambo_ready
    domain = [Simulation]
    range = [ComputationalMethod]

class use_algorithm(ObjectProperty):
    namespace = mambo_ready
    domain = [ComputationalMethod]
    range = [Algorithm]

# class has_ensemble(ObjectProperty):
#     namespace = mambo_ready
#     domain = [MolecularDynamics]
#     range = []

# EXPERIMENT
class has_experimental_input(ObjectProperty):
    namespace = mambo_ready
    domain = [Experiment]
    range = [Property, Structure]

class has_experimental_output(ObjectProperty):
    namespace = mambo_ready
    domain = [Experiment]
    range = [Property, Structure]

class is_measured_by(ObjectProperty):
    namespace = mambo_ready
    domain = [Property, Structure]
    range = [Experiment]
    inverse_property = has_experimental_output

class use_experimental_method(ObjectProperty):
    namespace = mambo_ready
    domain = [Experiment]
    range = [ExperimentalMethod]

# DATA PROPERTIES
class purpose(DataProperty):
    namespace = mambo_ready
    domain = [Material]
    range = [str]

class spacegroup(DataProperty):
    namespace = mambo_ready
    domain = [Structure]
    range = [str]

class unit(DataProperty):
    namespace = mambo_ready
    domain = [Property]
    range = [str]

class value(DataProperty):
    namespace = mambo_ready
    domain = [Property]
    range = [float]

class log(DataProperty):
    namespace = mambo_ready
    domain = [Experiment]
    range = [str]

class number_of_molecules(DataProperty):
    namespace = mambo_ready
    domain = [MolecularAggregate]
    range = [int]

class ID(DataProperty):
    namespace = mambo_ready
    domain = [Simulation]
    range = [str]

class log(DataProperty):
    namespace = mambo_ready
    domain = [Experiment]
    range = [str]

class atomic_number(DataProperty):
    namespace = mambo_ready
    domain = [Atom]
    range = [int]

class charge(DataProperty):
    namespace = mambo_ready
    domain = [Atom, MolecularSystem, StructuralUnit, Particle]
    range = [float]

class symbol(DataProperty):
    namespace = mambo_ready
    domain = [Atom]
    range = [str]

class composition(DataProperty):
    namespace = mambo_ready
    domain = [MolecularSystem]
    range = [str]

class formula(DataProperty):
    namespace = mambo_ready
    domain = [MolecularSystem, StructuralUnit, Particle]
    range = [str]

class algorithm_type(DataProperty):
    namespace = mambo_ready
    domain = [Algorithm]
    range = [str]

class energy_threshold(DataProperty):
    namespace = mambo_ready
    domain = [Algorithm]
    range = [float]

class force_threshold(DataProperty):
    namespace = mambo_ready
    domain = [Algorithm]
    range = [float]

class max_number_of_steps(DataProperty):
    namespace = mambo_ready
    domanin = [Algorithm]
    range = [int]

class timestep(DataProperty):
    namespace = mambo_ready
    domain = [Algorithm]
    range = [float]





# SAVE ONTOLOGY
mambo_ready.save(file="./mambo_ready.owl")

os.system("python src/inspect_mambo.py mambo_ready.owl")
