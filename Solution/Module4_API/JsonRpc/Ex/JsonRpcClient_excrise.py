#https://gurujsonrpc.appspot.com/

#https://gurujsonrpc.appspot.com/guru      (test server)
#Request JSON String
 #"method" : "guru.test", "params" : [ "name" ], "id" : 123 }

import requests
import json


def main():
    url = "https://gurujsonrpc.appspot.com/guru"
    headers = {'content-type': 'application/json'}
    
    someString="Python JSON"
    # Example echo method
    payload = {
        "method": "guru.test",
        "params": [someString],
        "jsonrpc": "2.0",
        "id": 123,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
    print(response["result"])

    #assert response["result"] == "echome!"
    #assert response["jsonrpc"] == "2.0"
    #assert response["id"] == 0

 

if __name__ == "__main__":
    main()
