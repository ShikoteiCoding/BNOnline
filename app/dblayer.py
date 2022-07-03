from pgmpy.readwrite import BIFReader, BIFWriter, UAIReader, UAIWriter, XMLBIFReader, XMLBIFWriter
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
    'UAI': {
        'reader': UAIReader,
        'writer': UAIWriter,
        'ext': '.uai'
    },
    'XMLBIF': {
        'reader': XMLBIFReader,
        'writer': XMLBIFWriter,
        'ext': '.xml'
    }
}

def extract_file_name(name: str) -> str:
    """ Extract filename without extension. """
    return name.split(".")[0]

def get_network_names() -> list[str]:
    """ Return the existing network names. """
    return [extract_file_name(f) for f in listdir(DATABASE_PATH) if isfile(join(DATABASE_PATH, f))]

def save_network(model: BayesianNetwork, serializer: str = 'BIF') -> None:
    """ Save a given network the 'database' """

    if not serializer in SERIALIZER.keys(): raise KeyError(f"Your key {serializer} does not exist.")

    filename = model.name

    writer = SERIALIZER[serializer]["writer"](model)
    extension = SERIALIZER[serializer]["ext"]
    serialization = writer.__str__()
    with open(DATABASE_PATH + filename + extension, "w") as f:
        f.write(serialization)

def read_network(name: str, serializer: str) -> str:
    """ Save a given network the 'database' """

    return ""