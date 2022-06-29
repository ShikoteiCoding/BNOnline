from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from fastapi import FastAPI

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
    return {"message": bn}

@app.post("/api/v1/network")
async def network_create(bn_config: dict):
    """ Create a bayesian network. """
    print(bn_config)

@app.post("/api/v1/network/save")
async def network_save(bn_config: dict):
    """ Save a bayesian network. """
    print(bn_config)


## Defining Bayesian Structure
#model = BayesianNetwork([('Guest', 'Host'), ('Price', 'Host#
## Defining the CPDs:
#cpd_guest = TabularCPD('Guest', 3, [[0.33], [0.33], [0.33]])
#cpd_price = TabularCPD('Price', 3, [[0.33], [0.33], [0.33]])
#cpd_host = TabularCPD(
#    'Host', 
#    3, 
#    [
#        [0, 0, 0, 0, 0.5, 1, 0, 1, 0.5],
#        [0.5, 0, 1, 0, 0, 0, 1, 0, 0.5],
#        [0.5, 1, 0, 1, 0.5, 0, 0, 0, 0]
#    ],
#    evidence=['Guest', 'Price'], evidence_card=[3, 3]
#)
#
## Associating the CPDs with the network structure.
#model.add_cpds(cpd_guest, cpd_price, cpd_host)
#
#print(f"Model is valid: {model.check_model()}")