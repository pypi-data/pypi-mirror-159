import argparse
import os
from services.proteins_search_service import ProteinsSearchService
from services.path_validation import validate_path


def main():
    parser = argparse.ArgumentParser(description='annotations for protein sequences and structures')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-i', '--pdb-ids',
                       type=str,
                       nargs="*",
                       help="Returns annotations for the given PDB id")
    group.add_argument('-f', '--from-file',
                       type=argparse.FileType('r'),
                       help="Returns annotations for the PDB ids contained on a specified text file: Expect a single "
                            "PDB id per line (no commas)")
    parser.add_argument('-s', '--save-file',
                        type=str,
                        const=f"{os.getcwd()}/annotations.json",
                        nargs='?',
                        help="Results are exported to a default or specified json file location. Expect an .json "
                             "extension. Default: annotations.json at program root")

    args = parser.parse_args()
    validate_path(args.save_file)

    service = ProteinsSearchService()
    if args.pdb_ids:
        service.search(args.pdb_ids, args.save_file)
    if args.from_file:
        pdb_list = [i.rstrip() for i in args.from_file.readlines()]
        service.search(pdb_list, args.save_file)


if __name__ == '__main__':
    main()
