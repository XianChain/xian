from cometbft.abci.v1beta3.types_pb2 import ResponseInitChain
from xian.utils import store_genesis_block

import asyncio


def init_chain(self, req) -> ResponseInitChain:
    abci_genesis_state = self.genesis["abci_genesis"]
    asyncio.ensure_future(store_genesis_block(self.client.raw_driver, abci_genesis_state))

    return ResponseInitChain()
