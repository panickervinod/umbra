# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: umbra.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.protobuf.timestamp_pb2
from umbra.common.protobuf import umbra_pb2


class BrokerBase(abc.ABC):

    @abc.abstractmethod
    async def Run(self, stream: 'grpclib.server.Stream[umbra_pb2.Config, umbra_pb2.Report]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/umbra.Broker/Run': grpclib.const.Handler(
                self.Run,
                grpclib.const.Cardinality.UNARY_UNARY,
                umbra_pb2.Config,
                umbra_pb2.Report,
            ),
        }


class BrokerStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Run = grpclib.client.UnaryUnaryMethod(
            channel,
            '/umbra.Broker/Run',
            umbra_pb2.Config,
            umbra_pb2.Report,
        )


class ScenarioBase(abc.ABC):

    @abc.abstractmethod
    async def Run(self, stream: 'grpclib.server.Stream[umbra_pb2.Deploy, umbra_pb2.Built]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/umbra.Scenario/Run': grpclib.const.Handler(
                self.Run,
                grpclib.const.Cardinality.UNARY_UNARY,
                umbra_pb2.Deploy,
                umbra_pb2.Built,
            ),
        }


class ScenarioStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Run = grpclib.client.UnaryUnaryMethod(
            channel,
            '/umbra.Scenario/Run',
            umbra_pb2.Deploy,
            umbra_pb2.Built,
        )
