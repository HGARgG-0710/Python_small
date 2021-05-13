from sys import argv
import requests

address = argv[1]
query = requests.get(address.strip(), allow_redirects=True)
print(len(query.text.splitlines()))
