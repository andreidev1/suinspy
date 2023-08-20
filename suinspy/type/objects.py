"""Interfaces"""

from dataclasses import dataclass
from typing import Optional

from pysui.sui.sui_types.address import SuiAddress


@dataclass
class SuiNSContract:
    packageId: SuiAddress
    suins: SuiAddress
    registry: SuiAddress
    reverseRegistry: SuiAddress


@dataclass
class NameObject:
    expiration_timestamp_ms: int
    nft_id: SuiAddress
    target_address: SuiAddress
    id: SuiAddress
    owner: Optional[SuiAddress]
    content_hash: Optional[str]
