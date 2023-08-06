import requests

url = "https://mobidb.bio.unipd.it/api/download?acc="


class MobiDBClient:

    def missing_residues(self, uniprot_accession_id):
        response = requests.get(url + uniprot_accession_id)
        response.raise_for_status()
        return response.json()
