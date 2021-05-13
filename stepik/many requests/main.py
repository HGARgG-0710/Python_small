from sys import argv
from requests import get, Response

addr = argv[1]
word = argv[2]


def isSearchedWord(query: Response, word: str):
    return query.text.split(" ")[0] == word


query = get(addr, allow_redirects=True)

while not isSearchedWord(query, word):
    addr = addr[:addr.rfind("/") + 1] + query.text.strip()
    query = get(addr, allow_redirects=True)

print(query.text)
