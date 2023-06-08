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

