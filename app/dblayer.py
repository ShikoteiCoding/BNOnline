from pgmpy.readwrite import BIFReader, BIFWriter
from pgmpy.models import BayesianNetwork

from os import listdir
from os.path import isfile, join

DATABASE_PATH = 'database/'

SERIALIZER = {
    'BIF': {
        'reader': BIFReader,
        'writer': BIFWriter,
        'ext': '.bif'
    },
}

def extract_file_name(name: str) -> str:
    """ Extract filename without extension. """
    return name.split(".")[0]

def get_network_names() -> list[str]:
    """ Return the existing network names. """
    return [extract_file_name(f) for f in listdir(DATABASE_PATH) if isfile(join(DATABASE_PATH, f))]

def save_network(model: BayesianNetwork, filename: str, serializer: str) -> None:
    """ Save a given network the 'database' """

    if not serializer in SERIALIZER.keys(): raise KeyError(f"Your key {serializer} does not exist.")

    serialized_model = SERIALIZER[serializer]["writer"](model)
    serialized_model.write_bif(filename = DATABASE_PATH + filename)

def read_network(name: str, serializer: str) -> str:
    """ Save a given network the 'database' """

    return ""