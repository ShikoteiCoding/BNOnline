from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

from fastapi import FastAPI, Request

from dblayer import get_network_names, save_network
from parser import create_network_from_dict, valid_request

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

@app.get("/api/v1/network/all")
async def network_read():
    """ Get a bayesian network. """
    return {"message": get_network_names()}

@app.post("/api/v1/network/save")
async def network_save(payload: Request):
    """ Save a bayesian network. """
    req = await payload.json()

    if not valid_request(req):
        return {"message": f"Your post must contain a body and a bayesian network."}

    network_config = req["body"]["bayesian_network"]

    try:
        bn = create_network_from_dict(network_config)
        bn.check_model()
    except Exception as err:
        return {"message": str(err)}

    save_network(bn)
    return {"message": f"Network saved: '{bn.name}'"}