send() {
    curl -d @- localhost:8000
}

get_network_all() {
	curl -X GET http://localhost:8000/api/v1/network/all
}

post_network_save() {
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

## Messages to get information
get_network_names() {
	cat << ++ | get_network_all
	{
		"body": "hi"
	}
++
}

## Messages for json serialisation
# Post a Valid Network: 
save_network() {
    cat << ++ | post_network_save
{
	"body": {
		"bayesian_network": {
			"name": "Test-Post",
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