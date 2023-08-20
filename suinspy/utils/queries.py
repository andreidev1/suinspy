"""Query module"""

from pysui.sui.sui_builders.get_builders import GetObject
from pysui.sui.sui_clients.common import handle_result
from pysui.sui.sui_clients.sync_client import SuiClient


def get_owner(client: SuiClient, nft_id: str):
    """Get owner"""

    options: dict = {"showOwner": True}

    owner_response = handle_result(
        client.execute(GetObject(object_id=nft_id, options=options))
    )

    return owner_response.owner.address_owner


def get_avatar(client: SuiClient, nft_id: str):
    """Get avatar of an owner"""

    options: dict = {"showDisplay": True, "showOwner": True}
    owner_response = handle_result(
        client.execute(GetObject(object_id=nft_id, options=options))
    )
    return owner_response.display.data["image_url"]
