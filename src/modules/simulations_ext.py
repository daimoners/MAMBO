# SIMULATION ENSEMBLE
class SimulationEnsemble(Thing):
    namespace = mambo_ready

class NPT(SimulationEnsemble):
    pass

class NVT(SimulationEnsemble):
    pass

class NVE(SimulationEnsemble):
    pass

# EXTERNAL COUPLING
class ExternalCoupling(Thing):
    namespace = mambo_ready

class Barostat(ExternalCoupling):
    pass

class Thermostat(ExternalCoupling):
    pass

# INTEGRATOR
class Integrator(Thing):
    namespace = mambo_ready

