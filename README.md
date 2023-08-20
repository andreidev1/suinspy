# Sui Name Service Python SDK

Python Sui Name Service SDK Client - built by community with [pysui](https://github.com/FrankC01/pysui/)

## Quick Start

Install `suinspy`

`pip install suinspy`

`poetry add suinspy`

Using git support:

`pip install git+https://git@github.com/andreidev1/suinspy.git`

Configure `pysui` with your own data.

```py
from pysui.sui.sui_config import SuiConfig
from pysui.sui.sui_clients.sync_client import SuiClient

def cfg_user():
    """Config user"""
    cfg = SuiConfig.user_config(
        # Required
        rpc_url="https://fullnode.mainnet.sui.io:443/",
        # Must be a valid Sui keystring (i.e. 'key_type_flag | private_key_seed' )
        prv_keys=["AIUPxQvxM18QggDDdTO0D0OD6PNVvtet50072d1grIyl"],
        # Needed for subscribing
        ws_url="wss://fullnode.mainnet.sui.io:443/",
    )
    return cfg

cfg = cfg_user()
client = SuiClient(cfg)

```

Import `suinspy`
```py
from suinspy.client import SuiNsClient
```

Create an instance of SuinsClient and choose network type (`mainet`, `testnet` or `devnet`).

```py
suins = SuiNsClient(client, 'mainet')
```

Fetch a name object:
```py
suins.get_name_object("suins.sui")
```

Fetch a name object including the owner and avatar:

**_NOTE:_** `show_owner` and `show_avatar` arguments are optional.
```py
suins.get_name_object("suins.sui", show_owner=True, show_avatar=True)
```

Fetch a SuiAddress linked to a name:
```py
suins.get_address("suins.sui")
```

## Official SuiNS Resources

[Official SuiNS Website](https://suins.io/)

[Official SuiNS Discord](https://discord.gg/suinsdapp)

## Ask A Question

Join Our Community [discord](https://discord.gg/CUTen9zu5h)
