from etherscan.accounts import Account
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

address = '0xc477A619657469b034a28290aa0acd0c2b6075d5'

api = Account(address=address, api_key=key)
blocks = api.get_all_blocks_mined(offset=10000, blocktype='uncles')
print(blocks)
