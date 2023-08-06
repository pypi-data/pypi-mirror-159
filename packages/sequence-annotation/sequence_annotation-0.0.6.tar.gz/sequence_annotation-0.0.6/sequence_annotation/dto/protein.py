class Protein:

    def __init__(self, pdb_id, sequence, chains, missing_residues):
        self.pdb_id = pdb_id
        self.sequence = sequence
        self.chains = chains
        self.missing_residues = missing_residues
