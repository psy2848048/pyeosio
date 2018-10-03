from .json_rpc_wrapper import RPCWrapper
from .transaction_builder import TransactionBuilder
from .action import Action


class Suites(object):
    def __init__(self, wrapper, wallet_pass, public_key):
        self.rpc = wrapper
        self.wallet_pass = wallet_pass
        self.public_key = public_key

    def push_action(self, code, action_name, account, permission, params):
        try:
            self.rpc.wallet_unlock(self.wallet_pass)
        except:
            pass

        txBuilder = TransactionBuilder(self.rpc)
        is_ok, bin_param = self.rpc.chain_abi_json_to_bin(params)
        act = Action(code, action_name, account, permission, bin_param['binargs'])
        ready_tx, chain_id =  txBuilder.build_sign_transaction_request([act])
        is_ok, signed_transaction = self.rpc.wallet_sign_transaction(ready_tx, [self.public_key], chain_id)
        is_ok, ret = self.rpc.chain_push_transaction(signed_transaction)

        return ret
