from cometbft.abci.v1beta1.types_pb2 import ResponseInfo
from xian.utils import (
    get_latest_block_hash,
    get_latest_block_height,
)


def info(self, req) -> ResponseInfo:
    res = ResponseInfo()
    res.app_version = self.app_version
    res.version = req.version
    res.last_block_height = get_latest_block_height(self.client.raw_driver)
    res.last_block_app_hash = get_latest_block_hash(self.client.raw_driver)
    return res
