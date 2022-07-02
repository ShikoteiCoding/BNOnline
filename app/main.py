from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

from fastapi import FastAPI, Request

from dblayer import get_network_names
from parser import parse_name, parse_structure

app = FastAPI()

bn = BayesianNetwork()

@app.on_event("startup")
def open_pool():
    print("Server started")

@app.on_event("shutdown")
def close_pool():
    print("Server closed")

@app.get("/api/v1/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/v1/network")
async def network_read():
    """ Get a bayesian network. """
    return {"message": "NotImplementedError"}

@app.post("/api/v1/network/save")
async def network_save(payload: Request):
    """ Save a bayesian network. """
    req = await payload.json()
    body = req["body"]

    print(body)

    bayesian_network = body["bayesian_network"]
    name = bayesian_network["name"]

    #if name in get_network_names(): print(f"Network {name} already exist")

    structure = parse_structure(bayesian_network)
    bn = BayesianNetwork(structure)
    bn.name = name
    try:
        bn.check_model()
    except Exception as err:
        return {"message": str(err)}
    return {"message": "BN Created"}