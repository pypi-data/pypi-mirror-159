import requests
from requests import HTTPError

from utils.pretty_print import PrettyPrint

url = "https://www.ebi.ac.uk/pdbe/api/"
entry_url = url + "pdb/entry/"
pdb_to_uniprot_mapping_url = "mappings/uniprot/"


class SiftsPDBClient:

    def __basic_get_call(self, base_url, domain, pdb_id):
        try:
            response = requests.get(base_url + domain + "/" + pdb_id)
            response.raise_for_status()
            return response.json()
        except HTTPError:
            if domain == "secondary_structure":
                PrettyPrint.warning_output(f"WARNING: The secondary structure for {pdb_id.upper()} could not be found")
            else:
                PrettyPrint.fail_output(f"ERROR: Could not find info for {pdb_id.upper()}. Verify input.")
                exit(1)

    def summary_by_pdb_id(self, pdb_id):
        return self.__basic_get_call(entry_url, "summary", pdb_id)

    def molecules_by_pdb_id(self, pdb_id):
        return self.__basic_get_call(entry_url, "molecules", pdb_id)

    def secondary_structure_by_pdb_id(self, pdb_id):
        return self.__basic_get_call(entry_url, "secondary_structure", pdb_id)

    def mappings_by_pdb_id(self, pdb_id):
        return self.__basic_get_call(url, "mappings", pdb_id)

    def residue_listing_by_pdb_id(self, pdb_id):
        return self.__basic_get_call(entry_url, "residue_listing", pdb_id)

    def uniprot_data_by_pdb_id(self, pdb_id):
        return self .__basic_get_call(url, pdb_to_uniprot_mapping_url, pdb_id)
