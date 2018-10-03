import json
import requests
import urllib.parse

from . import endpoints


class RPCWrapper(object):
    def __init__(self, api_endpoint, wallet_endpoint):
        self.api_endpoint = api_endpoint
        self.wallet_endpoint = wallet_endpoint

    def request(self, endpoint, uri, body=None):
        url = urllib.parse.urljoin(endpoint, uri)

        payloads = ""
        if body:
            payloads = json.dumps(body)
        else:
            payloads = None

        headers = {"Content-Type": "application/json"}
        if body:
            resp_obj = requests.post(url, data=payloads, headers=headers)
        else:
            resp_obj = requests.post(url, headers=headers)

        is_ok = True if resp_obj.status_code == 200 else False
        resp = resp_obj.json()
        return is_ok, resp

    def api_request(self, uri, body=None):
        return self.request(self.api_endpoint, uri, body)

    def wallet_request(self, uri, body=None):
        return self.request(self.wallet_endpoint, uri, body)

    # Wallet
    def wallet_lock(self, wallet='default'):
        return self.wallet_request(endpoints.WALLET_LOCK, wallet)

    def wallet_unlock(self, key, wallet='default'):
        return self.wallet_request(endpoints.WALLET_UNLOCK, [wallet, key])

    def wallet_open(self, wallet='default'):
        return self.wallet_request(endpoints.WALLET_OPEN, wallet)

    def wallet_get_public_keys(self):
        return self.wallet_request(endpoints.WALLET_GET_PUBLIC_KEYS)

    def wallet_sign_transaction(self, transaction, public_keys, chain_id):
        return self.wallet_request(
            endpoints.WALLET_SIGN_TRANSACTION, [transaction, public_keys, chain_id])

    # Chain
    def chain_get_info(self):
        return self.api_request(endpoints.CHAIN_GET_INFO)

    def chain_get_block(self, num_or_id):
        return self.api_request(endpoints.CHAIN_GET_BLOCK, {'block_num_or_id': num_or_id})

    def chain_abi_json_to_bin(self, abi_args):
        return self.api_request(endpoints.CHAIN_ABI_JSON_TO_BIN, abi_args)

    def chain_get_required_keys(self, transaction, available_keys):
        return self.api_request(endpoints.CHAIN_GET_REQUIRED_KEYS, {
            'transaction': transaction,
            'available_keys': available_keys
        })

    def chain_push_transaction(self, transaction):
        return self.api_request(endpoints.CHAIN_PUSH_TRANSACTION, {
            'transaction': transaction,
            'compression': 'none',
            'signatures': transaction['signatures']
        })

    # History
    def get_actions(self, position, offset, account_name):
        return self.api_request(endpoints.HISTORY_GET_ACTIONS, {
            'pos': position,
            'offset': offset,
            'account_name': account_name
        })

    def get_transaction(self, tx_id):
        return self.api_request(endpoints.HISTORY_GET_TRANSACTION, {
            'id': tx_id
        })

    def get_key_accounts(self, public_key):
        return self.api_request(endpoints.HISTORY_GET_KEY_ACCOUNTS, {
            'public_key': public_key
        })

    def get_controlled_accounts(self, controlling_account):
        return self.api_request(endpoints.HISTORY_GET_KEY_ACCOUNTS, {
            'controlling_account': controlling_account
        })

    # Net: Not yet implemented

    # Producer
    def pause(self):
        return self.api_request(endpoints.PRODUCER_PAUSE)

    def paused(self):
        return self.api_request(endpoints.PRODUCER_PAUSED)

    def resume(self):
        return self.api_request(endpoints.PRODUCER_RESUME)

    def get_runtime_options(self):
        return self.api_request(endpoints.PRODUCER_GET_RUNTIME_OPTIONS)

    def update_runtime_options(self):
        return self.api_request(endpoints.PRODUCER_UPDATE_RUNTIME_OPTIONS)

    # Db
    def db_size_get(self):
        return self.api_request(endpoints.DB_SIZE_GET)

