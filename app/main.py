from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

from fastapi import FastAPI, Request

from dblayer import get_network_names
from parser import parse_name, parse_structure, create_network_from_dict

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

    network_config = req["body"]["bayesian_network"]
    try:
        bn = create_network_from_dict(network_config)
        bn.check_model()
    except Exception as err:
        return {"message": str(err)}
    return {"message": "BN Created"}