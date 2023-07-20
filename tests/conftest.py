"""Configuration test file"""

import pytest

from pysui.sui.sui_config import SuiConfig
from pysui.sui.sui_clients.sync_client import SuiClient



def network_client():
    return dict(main=dict(rpc_url="https://fullnode.mainnet.sui.io:443/", ws_url="wss://fullnode.mainnet.sui.io:443/"),
                test=dict(rpc_url="https://fullnode.testnet.sui.io:443/", ws_url="wss://fullnode.testnet.sui.io:443/"),
                dev=dict(rpc_url="https://fullnode.devnet.sui.io:443/", ws_url="wss://fullnode.devnet.sui.io:443/")
                )
                

@pytest.fixture(scope='module')
def init_config():
    """Init config"""
    cfg = SuiConfig.user_config(
        # Required
        rpc_url=network_client()["test"]["rpc_url"],
        # Must be a valid Sui keystring (i.e. 'key_type_flag | private_key_seed' )
        prv_keys=["AIUPxQxvY18QggDDdTO0D0OD6PNVvtet50072d1grIyl"],
        # Needed for subscribing
        ws_url=network_client()["test"]["ws_url"]
    )
    return cfg


@pytest.fixture(scope='module')
def init_client(init_config):
    """Init client"""
    client = SuiClient(init_config)
    return client
