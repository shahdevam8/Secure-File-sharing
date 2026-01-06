import ipfshttpclient

def upload_to_ipfs(path):
    client = ipfshttpclient.connect()
    return client.add(path)["Hash"]
