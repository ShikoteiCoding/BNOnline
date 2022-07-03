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
			],
			"cpds": [
				["Guest", 3, [
					[0.33],
					[0.33],
					[0.33]
				]],
				["Price", 3, [
					[0.33],
					[0.33],
					[0.33]
				]],
				["Host", 3,
					[
						[0, 0, 0, 0, 0.5, 1, 0, 1, 0.5],
						[0.5, 0, 1, 0, 0, 0, 1, 0, 0.5],
						[0.5, 1, 0, 1, 0.5, 0, 0, 0, 0]
					],
					["Guest", "Price"],
					[3, 3]
				]
			]
		}
	}
}
++
}