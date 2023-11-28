from enum import Enum

class AtomType(Enum):
    ISOTYPE = 1
    RADIOACTIVE = 2
    ION = 3
    ANTIMATTER = 4
    STABLE = 5

class Atom:
    def __init__(self, name, atomic_mass_unit, neutrons, protons, electrons, atom_type):
        self.name = name
        self.atomic_mass_unit = atomic_mass_unit
        self.neutrons = neutrons
        self.protons = protons
        self.electrons = electrons
        self.atom_type = atom_type

    def isNeutral(self):
        return self.neutrons == self.electrons

    def __str__(self):
        return f"Name: {self.name}\nAtomic Mass Unit: {self.atomic_mass_unit}\nNeutrons: {self.neutrons}\nProtons: {self.protons}\nElectrons: {self.electrons}\nType: {self.atom_type}\n"

class Molecule:
    def __init__(self, name):
        self.name = name
        self.atoms = []

    def addAtom(self, atom):
        self.atoms.append(atom)

    def sortAtomsByMass(self):
        self.atoms.sort(key=lambda atom: atom.atomic_mass_unit)

    def findAverageMass(self):
        total_mass = sum(atom.atomic_mass_unit for atom in self.atoms)
        return total_mass / len(self.atoms) if len(self.atoms) > 0 else 0

    def __str__(self):
        atom_info = "\n".join([str(atom) for atom in self.atoms])
        return f"Molecule: {self.name}\nAtoms:\n{atom_info}\n"

# Приклад використання класів:
if __name__ == "__main__":
    hydrogen = Atom("Hydrogen", 1.008, 0, 1, 1, AtomType.STABLE)
    helium = Atom("Helium", 4.0026, 2, 2, 2, AtomType.STABLE)
    oxygen = Atom("Oxygen", 15.999, 8, 8, 8, AtomType.STABLE)

    molecule = Molecule("Water")
    molecule.addAtom(hydrogen)
    molecule.addAtom(hydrogen)
    molecule.addAtom(oxygen)

    print("Original Molecule:")
    print(molecule)

    molecule.sortAtomsByMass()
    print("Molecule after sorting by atomic mass:")
    print(molecule)

    average_mass = molecule.findAverageMass()
    print(f"Average atomic mass of the atoms in the molecule: {average_mass}")

    print(f"Is the hydrogen atom neutral? {hydrogen.isNeutral()}")
    print(f"Is the helium atom neutral? {helium.isNeutral()}")
