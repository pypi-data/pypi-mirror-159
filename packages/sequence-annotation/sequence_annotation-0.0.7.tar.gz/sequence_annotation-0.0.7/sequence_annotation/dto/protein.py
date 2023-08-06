class Protein:

    def __init__(self, pdb_id, related_uniprot_accessions, summary, pdb_sequence, chains, missing_residues=None):
        self.pdb_id = pdb_id
        self.related_uniprot_accessions = related_uniprot_accessions
        self.summary = summary
        self.pdb_sequence = pdb_sequence
        self.chains = chains
        self.missing_residues = missing_residues
