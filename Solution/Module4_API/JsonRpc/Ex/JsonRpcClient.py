import requests
import json


def main():
    url = "http://localhost:4000/jsonrpc"
    headers = {'content-type': 'application/json'}

    # Example echo method
    payload = {
        "method": "echo",
        "params": ["Welcom home!"],
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()

    print(response["result"])
    #assert response["result"] == "echome!"
    #assert response["jsonrpc"]
    #assert response["id"] == 0

    # Example add method
    payload = {
        "method": "add",
        "params": [10, 2],
        "jsonrpc": "2.0",
        "id": 1,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
    print(response["result"])

    # Example minus method
    payload = {
        "method": "minus",
        "params": [10, 2],
        "jsonrpc": "2.0",
        "id": 2,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
    print(response["result"])

if __name__ == "__main__":
    main()
