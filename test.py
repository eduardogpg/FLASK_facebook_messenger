from imgurpython import ImgurClient

client_id = '8add39161b124d5'
client_secret = '3633e2e1acfe8468ba951a1730bdbf63c9ef4ba3'

client = ImgurClient(client_id, client_secret)

# Example request
items = client.gallery()
for item in items:
    print(item.link)