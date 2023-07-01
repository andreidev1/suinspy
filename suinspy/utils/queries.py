
from pysui.sui.sui_builders.get_builders import GetObject
from pysui.sui.sui_clients.common import handle_result
from pysui.sui.sui_clients.sync_client import SuiClient
from suinspy.utils.config import client

def get_owner(client: SuiClient, nft_id: str):
    options: dict = {
        "showOwner" : True
    }

    owner_response = handle_result(client.execute(GetObject(object_id=nft_id, options=options)))
    #own = client.get_object("0x229738a3c32e744c3d3df6b7c7984fc09e60eb540cff3eefcb38a44d535ba8b8")
    #print(handle_result(own))
    return owner_response.owner.address_owner

print(get_owner(client=client, nft_id="0x229738a3c32e744c3d3df6b7c7984fc09e60eb540cff3eefcb38a44d535ba8b8"))

def get_avatar(client: SuiClient, avatar: str):
    options: dict = {
        "showDisplay": True,
        "showOwner" : True
    }
    owner_response = handle_result(client.execute(GetObject(object_id=avatar, options=options)))
    return owner_response.display.data["image_url"]

print(get_avatar(client=client, avatar="0x229738a3c32e744c3d3df6b7c7984fc09e60eb540cff3eefcb38a44d535ba8b8"))