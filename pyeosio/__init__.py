from .json_rpc_wrapper import RPCWrapper
from .suites import Suites

def init(api_endpoint, wallet_endpoint, wallet_key, public_key):
    global suite
    suite = Suites(
               RPCWrapper(api_endpoint, wallet_endpoint),
               wallet_key,
               public_key
            )
