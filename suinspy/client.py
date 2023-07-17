
import requests

from pysui.sui.sui_types.address import SuiAddress
from pysui.sui.sui_clients.sync_client import SuiClient
from pysui.sui.sui_builders.get_builders import GetDynamicFieldObject

from types.objects import SuiNSContract, NameObject
from utils.constants import GCS_URL, DEVNET_JSON_FILE, TESTNET_JSON_FILE
from utils.parser import parse_registry_response
from utils.queries import get_avatar, get_owner


class SuiNsClient:
    """Sui Name Service Client SDK"""

    def __init__(self, client: SuiClient, network_type: str, contract_objects = None):
        self.client = client
        self.network_type = network_type
    
    def get_suins_contract_objects(self) -> SuiNSContract:
        if self.client:
            if self.network_type == 'testnet':
                contract_url = GCS_URL + TESTNET_JSON_FILE
            if self.network_type == 'devnet':
                contract_url = GCS_URL + DEVNET_JSON_FILE

            response = requests.get(contract_url)
        
            if response.status_code == 200:
                self.contract_objects = response.json()
                
        return self.contract_objects

    def get_dynamic_field_object(self, parent_object_id: SuiAddress, key: None, type="0x1::string::String"):
        
        dynamic_field_object = GetDynamicFieldObject(
            parent_object_id,
            dict(type=type, value=key)
        )

        return dynamic_field_object 


    
    def get_name_object(self, name: str, show_owner=False, show_avatar=False) -> NameObject:
        
        [top_level_domain, domain] = name.split('.')[::-1]

        self.get_suins_contract_objects()


        build_registry_response = self.get_dynamic_field_object(
            self.contract_objects["registry"],
            [top_level_domain, domain],
            f'{self.contract_objects["packageId"]}::domain::Domain'
            )
        
        registry_response = self.client.execute(build_registry_response)

        name_object = parse_registry_response(registry_response.__dict__)

        nft_id = name_object["nft_id"]

        if show_owner == True:
            
            owner = get_owner(self.client, nft_id)

            name_object.update(owner=owner)

        if show_avatar == True:

            avatar = get_avatar(self.client, nft_id)

            name_object.update(content_hash=avatar)

        return name_object
        
    def get_address(self, name: str) -> SuiAddress:

        owner_address = self.get_name_object(name, show_owner=True)["owner"]
        
        return owner_address

    """
    def get_name(self, address: SuiAddress):
        
        self.get_suins_contract_objects()
        print(self.contract_objects)
        build_reverse_registry_response = self.get_dynamic_field_object(
            self.contract_objects["reverseRegistry"],
            address,
            'address'
            )
        
        print(build_reverse_registry_response.__dict__)
        reverse_registry_response = self.client.execute(build_reverse_registry_response)

        return reverse_registry_response
    """