import requests

url = "https://rest.uniprot.org/uniprotkb/search?size=1&query="


class UniprotPDBClient:

    def full_info_by_pdb_id(self, pdb_id):
        response = requests.get(url + pdb_id)
        response.raise_for_status()
        return response.json()
