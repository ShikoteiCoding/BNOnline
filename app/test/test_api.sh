send() {
    curl -d @- localhost:8000
}

post() {
    curl -d @- -X POST http://localhost:8000/api/v1/network/save
}

# TC1: Valid "Device certificate is valid but has changed" msg
tc1() {
    cat << ++ | post
        {
            "body": {
                "name": "Test Post"
            }
        }
++
}