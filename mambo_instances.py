from owlready2 import *

onto = get_ontology("./mambo.owl").load(reload=True)
print(list(onto.classes()))

with onto: 
    # Instances of `Atom` class
    atom1 = onto.Atom("Hydrogen")
    atom1.symbol = "H"
    atom1.name = "Hydrogen"
    atom1.atomic_weight = 1
    #atom1.isPartOfParticle = Particle()
    atom2 = onto.Atom("Helium")
    atom2.symbol = "He"
    atom2.name = "Helium"
    atom2.atomic_weight = 2
    #atom2.isPartOfParticle = Particle()

onto.save(file="./mambo.owl", format="rdfxml")
