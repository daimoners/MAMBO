# COORDINATES
class Coordinates(Thing):
    namespace = mambo_ready

class CartesianCoordinates(Coordinates):
    pass

class SphericalCoordinates(Coordinates):
    pass

# ORIENTATION
class Orientation(Thing):
    namespace = mambo_ready

class Quaternion(Orientation):
    pass

class RotationMatrix(Orientation):
    pass

# TOPOLOGY
class TopologicalEntities(Thing):
    namespace = mambo_ready

class Angle(TopologicalEntities):
    pass

class Bond(TopologicalEntities):
    pass

class Dihedral(TopologicalEntities):
    pass

# LATTICE PARAMETER
class LatticeParameter(Thing):
    namespace = mambo_ready
