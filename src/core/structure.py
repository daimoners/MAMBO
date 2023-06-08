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
