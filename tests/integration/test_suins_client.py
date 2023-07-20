from suinspy.client import SuiNsClient
from suinspy.types.objects import NameObject

def test_get_suins_contract_objects(init_client):

    stub_suins_client = SuiNsClient(
        client=init_client,
        network_type='testnet',         
        contract_objects=dict(
        packageId="0xa789edcd4419bd9b3296afe6be7e537f985bebd48a2793530267e746221a8e56",
        registry="0x6e7e165b58b6f18bf87c438865d9ffc7722562c351bdca7b10a190cf33976308",
        reverseRegistry="0xc20a41b333f7955bf22bd46846318c979e3530e14f5913956d2debe17135139e",
        suins="0xdf5a2bcc7dcd60e89a956d554e3392dc50df1b1bb40048663102cbda0160590c"
        )
    )

    suins = SuiNsClient(client=init_client, network_type='testnet')

    contract_objects = suins.get_suins_contract_objects()

    assert stub_suins_client.contract_objects == contract_objects


def test_get_name_object(init_client):
    stub_name_object = NameObject(
        expiration_timestamp_ms='1716366440521',
        nft_id="0x229738a3c32e744c3d3df6b7c7984fc09e60eb540cff3eefcb38a44d535ba8b8",
        target_address=None,
        id="0x8196d35f40c39ff44b52d9ce6858ae5eb87070405bad919d1d03425aa98ab5bc",
        owner="0x478a3aa22f112f33b5454a2ca865621878d4a493e6f7e7e678ebe61cbf0efdb5",
        content_hash="ipfs://QmaLFg4tQYansFpyRqmDfABdkUVy66dHtpnkH15v1LPzcY",
    ).__dict__

    suins_client = SuiNsClient(client=init_client, network_type='testnet')

    name_object = suins_client.get_name_object("suins.sui", show_owner=True, show_avatar=True)

    assert stub_name_object == name_object