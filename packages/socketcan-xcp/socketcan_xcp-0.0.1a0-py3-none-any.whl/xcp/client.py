""" module:: xcp.client
    :platform: Any
    :synopsis: XCP Client originally called Master specification
    moduleauthor:: Patrick Menschel (menschel.p@posteo.de)
    license:: GPL v3
"""
import logging
from queue import Queue
from threading import Thread
from enum import IntEnum
from typing import Union

from xcp.transport import XcpOnCan
from xcp.protocol import XCP_PROTOCOL_VERSION, parse_packet_from_server, PacketIdFromServer, concat_connect_command, \
    ConnectMode, StdCmd, parse_response_data, concat_disconnect_command, concat_get_comm_mode_info, \
    concat_get_status_command, ComModeBasicFlag


class XcpClientState(IntEnum):
    Init = 0
    NotConnected = 1
    Connected = 2


class XcpClient:
    """
    This class represents the XCP Master which is the client side of XCP.
    """

    def __init__(self, transport: Union[XcpOnCan, ]):
        """
        Constructor

        :param transport: A xcp transport instance.
        """
        self._logger = logging.getLogger(__name__)
        self.timeout = 1
        self._state = None
        self._protocol_layer_version = XCP_PROTOCOL_VERSION
        self._endianess = None

        self.state = XcpClientState.Init
        self.rx_queue = Queue()
        self.rx_handler = Thread(target=self.handle_rx)
        self.rx_handler.daemon = True
        self.transport = transport
        # do some init
        self.state = XcpClientState.NotConnected
        self.rx_handler.start()

    @property
    def state(self) -> XcpClientState:
        return self._state

    @state.setter
    def state(self, value: XcpClientState) -> None:
        self._state = value

    @property
    def endianess(self):
        return self._endianess

    @endianess.setter
    def endianess(self, value):
        self._logger.info("Set Endianess to '{0}'".format(value))
        self._endianess = value

    def handle_rx(self):
        """
        The thread handling incoming communication.
        It feeds into local receive queue where request mechanism checks for responses.
        :return: Nothing.
        """
        while True:
            data = self.transport.recv()
            msg = parse_packet_from_server(data=data)
            self.rx_queue.put(msg)  # FIXME: This must be a command queue only - refactor in order to enable DAQ later

    def request(self, req: Union[bytes, bytearray]):
        self.transport.send(req)
        resp = self.rx_queue.get(timeout=self.timeout)
        packet_id = resp.get("packet_id")
        if packet_id == PacketIdFromServer.Response:
            resp.update(parse_response_data(cmd=StdCmd(req[0]), data=resp.get("command_response_data"),
                                            endianess=self.endianess))
        elif packet_id == PacketIdFromServer.Error:
            pass
        elif packet_id == PacketIdFromServer.Event:
            pass
        elif packet_id == PacketIdFromServer.ServiceRequest:
            pass
        else:
            pass
        return resp

    def connect(self, mode: ConnectMode = ConnectMode.Normal):
        resp = self.request(req=concat_connect_command(mode=mode))
        if ComModeBasicFlag.MSBFirst in resp.get("com_mode_basic_flags"):
            self.endianess = "big"
        else:
            self.endianess = "little"
        return resp

    def disconnect(self):
        return self.request(req=concat_disconnect_command())

    def get_status(self):
        return self.request(req=concat_get_status_command())

    def get_comm_mode_info(self):
        return self.request(req=concat_get_comm_mode_info())
