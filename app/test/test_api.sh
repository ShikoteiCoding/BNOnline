send() {
    curl -d @- localhost:8000
}

post() {
    curl -d @- -X POST http://localhost:8000/api/v1/network/save
}

# TC0: Test post function
tc0() {
    cat << ++ | post
        {
            "body": {
                "name": "Test Post"
            }
        }
++
}

## Messages for json serialisation
# TC1: 
tc1() {
    cat << ++ | post
        {
            "body": {
                "bayesian_network": {
                    "name": "Test Post",
                    "structure": [
                        ["Guest", "Host"],
                        ["Price", "Host"]
                    ]
                }
            }
        }
++
}