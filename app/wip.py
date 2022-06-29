from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

if __name__ == "__main__":
    # Defining Bayesian Structure
    model = BayesianNetwork([('Guest', 'Host'), ('Price', 'Host')])
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

    print(f"Model is valid: {model.check_model()}")
    print(model.graph_attr_dict_factory.__dict__)