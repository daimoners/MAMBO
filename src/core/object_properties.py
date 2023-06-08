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
