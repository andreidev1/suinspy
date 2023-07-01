from pysui.sui.sui_config import SuiConfig
from pysui.sui.sui_clients.sync_client import SuiClient

def cfg_user():
    """Config user"""
    cfg = SuiConfig.user_config(
        # Required
        rpc_url="https://fullnode.testnet.sui.io:443/",
        # Must be a valid Sui keystring (i.e. 'key_type_flag | private_key_seed' )
        prv_keys=["AIUPxQveY18QggDDdTO0D0OD6PNVvtet50072d1grIyl"],
        # Needed for subscribing
        ws_url="wss://fullnode.testnet.sui.io:443/",
    )
    return cfg

cfg = cfg_user()
client = SuiClient(cfg)
my_sui_address = cfg.addresses[0]
