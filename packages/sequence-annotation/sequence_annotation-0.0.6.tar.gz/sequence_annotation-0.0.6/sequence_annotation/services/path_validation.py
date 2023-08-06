import os

def validate_path(path):
    if path:
        x = path.split("/")

        file_name = x.pop()
        ext = file_name.split(".").pop()

        result = "/".join(x)

        isValidPath = os.path.isdir(result)
        isValidFile  = ext == "json"

        if not isValidFile or not isValidPath:
            print("invalid path or file type, the file extension must be .json")
            exit()

