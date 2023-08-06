import json

from clients.mobidb_client import MobiDBClient
from clients.sifts_client import SiftsPDBClient
from clients.uniprot_client import UniprotPDBClient
from dto.chains import Chain, SecondaryStructure, Aminoacid
from dto.protein import Protein
from dto.residues import Residue
from utils.pretty_print import PrettyPrint


class ProteinsSearchService:
    sifts_client = SiftsPDBClient()
    uniprot_client = UniprotPDBClient()
    mobidb_client = MobiDBClient()

    def search(self, pdb_list, save_results):

        responses = []
        for pdb_id in pdb_list:
            print(f"Retrieving data for {pdb_id.upper()}...")
            protein = self.search_in_sites(pdb_id)
            if protein:
                responses.append(protein)

        if responses:
            if save_results:
                file_path = save_results
                output_file = open(file_path, "a")
                output_file.write(json.dumps(responses, indent=3))
                output_file.close()
                print(f"Output file saved as {file_path}")
            else:
                PrettyPrint.ok_output("\n" + json.dumps(responses, indent=3))

    def search_in_sites(self, pdb):

        pdb_id = pdb.lower()

        # Obtains the protein sequence and summary of its properties
        summary = self.sifts_client.summary_by_pdb_id(pdb_id).get(pdb_id)
        molecules = self.sifts_client.molecules_by_pdb_id(pdb_id)
        molecules_data = list(molecules[pdb_id])
        pdb_sequence = molecules_data[0].get('pdb_sequence')

        # Uniprot accessions for the given pdb id
        uniprot_accessions = self.sifts_client.uniprot_data_by_pdb_id(pdb_id).get(pdb_id).get("UniProt")
        related_uniprot_accessions = list(uniprot_accessions.keys())

        # Missing residues per protein chain
        missing_residues = self.found_missing_residues(pdb_id, related_uniprot_accessions)

        # Obtains the chains, residues and secondary structures
        residues = self.sifts_client.residue_listing_by_pdb_id(pdb_id)
        residues_data = list(residues[pdb_id].get('molecules'))
        residues_chains = residues_data[0].get('chains')

        chains_and_residues = self.get_chains_composition(residues_chains, pdb_id)

        protein = Protein(pdb_id.upper(), related_uniprot_accessions, summary, pdb_sequence, chains_and_residues,
                          missing_residues)

        return protein.__dict__

    def get_chains_composition(self, residues_chains, pdb_id):

        chains_and_residues = []

        for c in residues_chains:
            residues_response = []
            chain = Chain(c.get('chain_id'))
            for amins in c.get('residues'):
                r = Residue(amins.get('residue_name'), amins.get('author_residue_number'))
                residues_response.append(r.__dict__)
            chain.residues = residues_response

            self.found_secondary_struct(chain, pdb_id)

            chains_and_residues.append(chain.__dict__)

        return chains_and_residues

    def found_missing_residues(self, pdb_id, uniprot_accession_ids):
        mobidb_annotations = [self.mobidb_client.missing_residues(accession_id) for accession_id in
                              uniprot_accession_ids]

        missing_residues = {}

        for annotation in mobidb_annotations:
            current_acc_data = {
                annotation.get("acc"): [dict((k, v) for k, v in annotation.items() if
                                             all(keyword in k for keyword in ["missing_residues", pdb_id]))]
            }

            for key in current_acc_data:
                for elem in current_acc_data[key]:
                    if elem:
                        current_chain_id = list(elem.keys())[0]
                        missing_residues[current_chain_id] = elem.get(current_chain_id)
                        missing_residues[current_chain_id]["uniprot_source"] = key

        return missing_residues

    def found_secondary_struct(self, chain, pdb_id):
        # Obtains which residues are part of helices or strands

        second_struct = self.sifts_client.secondary_structure_by_pdb_id(pdb_id)

        if not second_struct:
            chain.secondary_structure = SecondaryStructure().__dict__
            return

        ss_data = list(second_struct[pdb_id].get('molecules'))
        second_struct_info = ss_data[0].get('chains')

        helices = []
        strands = []
        structure = SecondaryStructure()

        for s in second_struct_info:
            if s.get('chain_id') == chain.chain_id:

                for h in s.get('secondary_structure').get('helices'):
                    a = Aminoacid()
                    a.residue_number_start = h.get('start').get('residue_number')
                    a.residue_number_end = h.get('end').get('residue_number')
                    helices.append(a.__dict__)

                for p in s.get('secondary_structure').get('strands'):
                    a = Aminoacid()
                    a.residue_number_start = p.get('start').get('residue_number')
                    a.residue_number_end = p.get('end').get('residue_number')
                    strands.append(a.__dict__)
                structure.helices = helices
                structure.strands = strands

        chain.secondary_structure = structure.__dict__

