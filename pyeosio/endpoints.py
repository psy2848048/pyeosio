# Wallet API removed from v1.2.0
WALLET_OPEN = '/v1/wallet/open'
WALLET_UNLOCK = 'v1/wallet/unlock'
WALLET_LOCK = 'v1/wallet/lock'
WALLET_SIGN_TRANSACTION = 'v1/wallet/sign_transaction'
WALLET_GET_PUBLIC_KEYS = 'v1/wallet/get_public_keys'

CHAIN_GET_INFO = 'v1/chain/get_info'
CHAIN_GET_BLOCK = 'v1/chain/get_block'
CHAIN_PUSH_TRANSACTION = 'v1/chain/push_transaction'
CHAIN_PUSH_TRANSACTIONS = 'v1/chain/push_transactions'
CHAIN_ABI_JSON_TO_BIN = 'v1/chain/abi_json_to_bin'
CHAIN_GET_REQUIRED_KEYS = 'v1/chain/get_required_keys'

HISTORY_GET_ACTIONS = 'v1/history/get_actions'
HISTORY_GET_TRANSACTION = 'v1/history/get_transaction'
HISTORY_GET_KEY_ACCOUNTS = 'v1/history/get_key_accounts'
HISTORY_GET_CONTROLLED_ACCOUNTS = 'v1/history/get_controlled_accounts'

NET_CONNECT = "v1/net/connect"
NET_DISCONNECT = "v1/net/disconnect"
NET_CONNECTIONS = "v1/net/connections"
NET_STATUS = "v1/net/status"

PRODUCER_PAUSE = "v1/producer/pause"
PRODUCER_RESUME = "v1/producer/resume"
PRODUCER_PAUSED = "v1/producer/paused"
PRODUCER_GET_RUNTIME_OPTIONS = "v1/producer/get_runtime_options"
PRODUCER_UPDATE_RUNTIME_OPTIONS = "v1/producer/update_runtime_options"
#PRODUCER_GET_GREYLIST = "v1/producer/get_greylist"
#PRODUCER_ADD_GREYLIST_ACCOUNTS = "v1/producer/add_greylist_accounts"
#PRODUCER_REMOVE_GREYLIST_ACCOUNTS = "v1/producer/remove_greylist_accounts"
#PRODUCER_GET_WHITELISTT_BLACKLIST = "v1/producer/remove_greylist_accounts"

DB_SIZE_GET = "v1/db_size/get"
