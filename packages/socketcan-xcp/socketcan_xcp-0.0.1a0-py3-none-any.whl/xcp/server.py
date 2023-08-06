""" module:: xcp.slave
    :platform: Any
    :synopsis: XCP Server originally called Slave in specification
    moduleauthor:: Patrick Menschel (menschel.p@posteo.de)
    license:: GPL v3
"""
import logging
from threading import Thread
from enum import IntEnum
from typing import Union

from xcp.transport import XcpOnCan
from xcp.protocol import parse_packet_from_client, StdCmd, concat_connect_response, ResourceFlag, ComModeBasicFlag, \
    XCP_PROTOCOL_VERSION, concat_response_packet, SessionStatus, ProtectionStatus, concat_status_response, \
    concat_comm_mode_info_response, ComModeOptional


class XcpServerState(IntEnum):
    Init = 0
    NotConnected = 1
    Connected = 2


class XcpServer:
    """
    This class represents the XCP Slave which is the server side of XCP.
    This implementation is, for now intended to work as a mock to test the client side.
    Therefore implementation only includes standard / non-optional services.
    The resume Mode is also omitted for now.
    """

    def __init__(self,
                 transport: Union[XcpOnCan, ],
                 endianess: str = "big"):
        """
        Constructor

        :param transport: A xcp transport instance.
        :type transport: XcpOnCan
        :param endianess: The endianess to use for built-in int-bytes conversion.
        :type endianess: str
        """
        self._logger = logging.getLogger(__name__)
        self._state = XcpServerState.Init
        self._resource = ResourceFlag(0)
        self._endianess = endianess
        self._com_mode_basic = ComModeBasicFlag(0)
        if self.endianess == "big":
            self._com_mode_basic |= ComModeBasicFlag.MSBFirst
        self._max_cto = 8
        self._max_dto = 8
        self._protocol_layer_version = XCP_PROTOCOL_VERSION
        self._session_status = SessionStatus(0)
        self._protection_status = ProtectionStatus(0)
        self._session_config_id = 0

        self._com_mode_optional = ComModeOptional(0)
        self._max_bs = 255
        self._min_st = 0
        self._queue_size = 255
        self._xcp_driver_version = 1.1  # what version should be here - Autosar Driver Version ?!

        self.rx_handler = Thread(target=self.handle_rx)
        self.rx_handler.daemon = True
        self.transport = transport
        # do some init
        self.state = XcpServerState.NotConnected
        self.rx_handler.start()

    @property
    def state(self) -> XcpServerState:
        return self._state

    @state.setter
    def state(self, value: XcpServerState) -> None:
        if self._state != value:
            self._logger.info("State Change {0} -> {1}".format(self._state.name, value.name))
            self._state = value

    @property
    def resource(self):
        return self._resource

    @property
    def com_mode_basic(self):
        return self._com_mode_basic

    @property
    def max_cto(self):
        return self._max_cto

    @property
    def max_dto(self):
        return self._max_dto

    @property
    def protocol_layer_version(self):
        return self._protocol_layer_version

    @property
    def protection_status(self):
        return self._protection_status

    @property
    def session_status(self):
        return self._session_status

    @property
    def session_config_id(self):
        return self._session_config_id

    @property
    def endianess(self):
        return self._endianess

    @property
    def com_mode_optional(self):
        return self._com_mode_optional

    @property
    def max_bs(self):
        return self._max_bs

    @property
    def min_st(self):
        return self._min_st

    @property
    def queue_size(self):
        return self._queue_size

    @property
    def xcp_driver_version(self):
        return self._xcp_driver_version

    def handle_rx(self):
        """
        The thread handling incoming communication.

        It reacts on the commands from a client.
        :return: Nothing.
        """
        while True:
            data = self.transport.recv()
            msg = parse_packet_from_client(data=data)
            command = msg.get("packet_id")
            if command == StdCmd.Connect:
                self.on_connect()
            elif command == StdCmd.Disconnect:
                self.on_disconnect()

            elif command == StdCmd.GetStatus:
                self.on_get_status()

            elif command == StdCmd.GetCommModeInfo:
                self.on_get_comm_mode_info()

            else:
                self._logger.error("Unhandled Command {0}".format(command.name))

    def on_connect(self) -> None:
        """
        Connect

        :return: Nothing.
        """
        self._logger.debug("Connect")
        self.transport.send(
            concat_response_packet(command_response_data=concat_connect_response(
                resource=self.resource,
                com_mode_basic=self.com_mode_basic,
                max_cto=self.max_cto,
                max_dto=self.max_dto,
                protocol_layer_version=self.protocol_layer_version,
                transport_layer_version=self.transport.transport_layer_version,
            )))
        self.state = XcpServerState.Connected

    def on_disconnect(self) -> None:
        """
        Disconnect

        :return: Nothing.
        """
        self._logger.debug("Disconnect")
        self.transport.send(concat_response_packet())
        self.state = XcpServerState.NotConnected

    def on_get_status(self):
        self._logger.debug("Get Status")
        self.transport.send(
            concat_response_packet(command_response_data=concat_status_response(
                session_status=self.session_status,
                resource_protection_status=self.protection_status,
                session_config_id=self.session_config_id,
                endianess=self.endianess
            )))

    def on_get_comm_mode_info(self):
        self._logger.debug("Comm Mode Info")
        self.transport.send(
            concat_response_packet(command_response_data=concat_comm_mode_info_response(
                comm_mode_optional=self.com_mode_optional,
                max_bs=self.max_bs,
                min_st=self.min_st,
                queue_size=self.queue_size,
                xcp_driver_version=self.xcp_driver_version,
            )))
