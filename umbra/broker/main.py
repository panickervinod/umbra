import json
import asyncio
import logging

from umbra.common.protobuf.umbra_grpc import BrokerBase
from umbra.broker.operator import Operator


logger = logging.getLogger(__name__)


class Broker(BrokerBase):
    def __init__(self, info):
        self.info = info
        self.operator = Operator(info)
    
    async def Run(self, stream):
        request = await stream.recv_message()
        reply = await self.operator.run(request)
        await stream.send_message(reply)