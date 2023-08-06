import requests
from requests import HTTPError

from utils.pretty_print import PrettyPrint

url = "https://mobidb.bio.unipd.it/api/download?acc="


class MobiDBClient:

    def missing_residues(self, uniprot_accession_id):
        try:
            response = requests.get(url + uniprot_accession_id)
            response.raise_for_status()
            return response.json()
        except HTTPError:
            PrettyPrint.warning_output(f"WARNING: The missing residues for {uniprot_accession_id.upper()} could not be found")

