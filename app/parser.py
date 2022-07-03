from typing import Any
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

def create_network_from_dict(config: dict) -> BayesianNetwork:
    """ From a json response. Build the Bayesian network. """
    bn = BayesianNetwork(parse_structure(config))
    bn.name = parse_name(config)

    cpds = []
    for cpd in parse_cpds(config):
        cpds.append(TabularCPD(*cpd))

    bn.add_cpds(*cpds)

    return bn





def parse_name(config: dict) -> str | None:
    return config.get("name")

def parse_structure(config: dict) -> str | None:
    return config.get("structure")

def parse_cpds(config: dict) -> list[list[Any]]:
    return config.get("cpds") or []