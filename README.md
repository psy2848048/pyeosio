# pyeosio

EOSIO JSON RPC Wrapper

---

## Install

```python
git clone https://github.com/psy2848048/pyeosio.git
python3 setup.py install
```

## Usage

```python
import pyeosio
pyeosio.init("your_nodeos_address", "your_keosd_address", "your_default_wallet_password", "your_public_key")

# All-in-one suite
pyeosio.suite.push_action("bryanrhee", "recorddata", "bryanrhee", "active", {"code":"bryanrhee", "action":"recorddata", "args": {"user": "bryanrhee", "data": "test"}})
```

## ToDo

1. Suites
   1. push_actions
   1. get_table_rows
1. Add test
1. Travis-ci integration
