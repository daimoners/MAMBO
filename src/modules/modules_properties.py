class has_bond(ObjectProperty):
    namespace = mambo_ready
    domain = [MolecularSystem, StructuralUnit]
    range = [Bond]

class has_angle(ObjectProperty):
    namespace = mambo_ready
    domain = [MolecularSystem, StructuralUnit]
    range = [Angle]

class has_dihedral(ObjectProperty):
    namespace = mambo_ready
    domain = [MolecularSystem, StructuralUnit]
    range = [Dihedral]

class has_COM_coordinates(ObjectProperty):
    namespace = mambo_ready
    domain = [MolecularSystem]
    range = [CartesianCoordinates, SphericalCoordinates]

class corresponds_to_dihedral(ObjectProperty):
    namespace = mambo_ready
    domain = [FourBody]
    range = [Dihedral]

class corresponds_to_angle(ObjectProperty):
    namespace = mambo_ready
    domain = [ThreeBody]
    range = [Angle]
    # inverse_property

class corresponds_to_bond(ObjectProperty):
    namespace = mambo_ready
    domain = [TwoBody]
    range = [Bond]

class has_barostat(ObjectProperty):
    namespace = mambo_ready
    domain = [Algorithm]
    range = [Barostat]

class first_atom(ObjectProperty):
    namespace = mambo_ready
    domain = [Angle, Bond, Dihedral]
    range = [Atom]

class second_atom(ObjectProperty):
    namespace = mambo_ready
    domain = [Angle, Bond, Dihedral]
    range = [Atom]

class third_atom(ObjectProperty):
    namespace = mambo_ready
    domain = [Bond, Dihedral]
    range = [Atom]

class fourth_atom(ObjectProperty):
    namespace = mambo_ready
    domain = [Dihedral]
    range = [Atom]

class has_component(ObjectProperty):
    namespace = mambo_ready
    domain = [BondedPotential, NonBondedPotential]
    range = [PotentialComponent]

