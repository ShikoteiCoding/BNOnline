from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

from dblayer import save_network, read_network, get_network_names, SERIALIZER

def create_bn() -> BayesianNetwork:
    # Defining Bayesian Structure
    model = BayesianNetwork([('Guest', 'Host'), ('Price', 'Host')])
    model.name = "Test Network"
    # Defining the CPDs:
    cpd_guest = TabularCPD('Guest', 3, [[0.33], [0.33], [0.33]])
    cpd_price = TabularCPD('Price', 3, [[0.33], [0.33], [0.33]])
    cpd_host = TabularCPD(
        'Host', 
        3, 
        [
            [0, 0, 0, 0, 0.5, 1, 0, 1, 0.5],
            [0.5, 0, 1, 0, 0, 0, 1, 0, 0.5],
            [0.5, 1, 0, 1, 0.5, 0, 0, 0, 0]
        ],
        evidence=['Guest', 'Price'], evidence_card=[3, 3]
    )

    # Associating the CPDs with the network structure.
    model.add_cpds(cpd_guest, cpd_price, cpd_host)

    return model


def test_write():
    model = create_bn()

    for key in SERIALIZER.keys():
        save_network(model, key)

def test_files():
    print(get_network_names())

def test_serialize():
    model = create_bn()
    print(model)


if __name__ == "__main__":
    test_serialize()