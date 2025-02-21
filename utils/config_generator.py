import json

def generate_config(protocol, server_address, port, uuid):
    config = {
        "v": "2",
        "ps": "Example",
        "add": server_address,
        "port": port,
        "id": uuid,
        "aid": "0",
        "net": protocol,
        "type": "none",
        "host": "",
        "path": "",
        "tls": ""
    }
    return json.dumps(config)