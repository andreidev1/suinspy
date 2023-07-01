
import json
from typing import List

import requests

from pysui.sui.sui_types.address import SuiAddress
from pysui.sui.sui_clients.sync_client import SuiClient
from pysui.sui.sui_builders.get_builders import GetDynamicFieldObject, GetDynamicFields

from utils.constants import GCS_URL, DEVNET_JSON_FILE, TESTNET_JSON_FILE
from utils.config import client

AVATAR_NOT_OWNED = 'AVATAR_NOT_OWNED'


class SuiNsClient:
    """Sui Name Service Client SDK"""

    def __init__(self, client: SuiClient, contract_objects = None):
        self.client = client
    
    def get_suins_contract_objects(self):
        if self.client:
            contract_url = GCS_URL + DEVNET_JSON_FILE
            response = requests.get(contract_url)

            self.contract_objects = response.json()
    

    def _get_dynamic_field_object(self, parent_object_id: SuiAddress, key: None, type="0x1::string::String"):
        
        dynamic_field_object = GetDynamicFieldObject({
            parent_object_id, 
            
            })
        
    
    def get_name_data(self, data_object_id: SuiAddress, fields: List):
        pass

    
    # def get_name_object()

    # def get_address()

    # def get_name()
suins = SuiNsClient(client)
print(suins.get_suins_contract_objects())