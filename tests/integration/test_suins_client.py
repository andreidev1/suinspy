"""Test against test network and main network"""
from suinspy.client import SuiNsClient
from suinspy.type.objects import NameObject

def test_get_suins_contract_objects_testnet(init_client):

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


def test_get_name_object_testnet(init_client):

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

def test_get_suins_contract_objects_mainet(init_client):

    stub_suins_client = SuiNsClient(
        client=init_client,
        network_type='mainet',         
        contract_objects=dict(
        packageId="0xd22b24490e0bae52676651b4f56660a5ff8022a2576e0089f79b3c88d44e08f0",
        registry="0xe64cd9db9f829c6cc405d9790bd71567ae07259855f4fba6f02c84f52298c106",
        reverseRegistry="0x2fd099e17a292d2bc541df474f9fafa595653848cbabb2d7a4656ec786a1969f",
        suins="0x6e0ddefc0ad98889c04bab9639e512c21766c5e6366f89e696956d9be6952871"
        )
    )

    suins = SuiNsClient(client=init_client, network_type='mainet')

    contract_objects = suins.get_suins_contract_objects()

    assert stub_suins_client.contract_objects == contract_objects
