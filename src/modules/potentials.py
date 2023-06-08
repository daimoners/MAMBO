# INTERACTION POTENTIAL
class InteractionPotential(Thing):
    namespace = mambo_ready

class MolecularMechanics(InteractionPotential):
    pass

class BondedPotential(MolecularMechanics):
    pass

class NonBondedPotential(MolecularMechanics):
    pass

class QuantumMechanics(InteractionPotential):
    pass

class DFT(QuantumMechanics):
    pass

class HartreeFock(QuantumMechanics):
    pass

# POTENTIAL COMPONENT
class PotentialComponent(Thing):
    namespace = mambo_ready

class FourBody(PotentialComponent):
    pass

class ThreeBody(PotentialComponent):
    pass

class TwoBody(PotentialComponent):
    pass

