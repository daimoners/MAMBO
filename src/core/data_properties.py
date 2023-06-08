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

