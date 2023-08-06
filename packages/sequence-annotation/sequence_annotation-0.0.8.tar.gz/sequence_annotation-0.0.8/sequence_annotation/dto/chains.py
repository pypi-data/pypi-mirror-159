class Chain:
    residues = []

    secondary_structure = None

    def __init__(self, chain_id):
        self.chain_id = chain_id


class SecondaryStructure:
    helices = []
    strands = []


class Aminoacid:
    residue_number_start: 0
    residue_number_end: 0
