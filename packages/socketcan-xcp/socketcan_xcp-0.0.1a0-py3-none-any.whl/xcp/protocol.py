""" module:: xcp.protocol
    :platform: Any
    :synopsis: XCP Protocol Layer
    moduleauthor:: Patrick Menschel (menschel.p@posteo.de)
    license:: GPL v3

    Note: XCP is a point to point communication protocol from a XCP Master to a XCP slave.
          The protocol strictly distinguishes Command Code meanings by direction.
          The Command Codes, i.e. bytes that switch program flow are present in both with different meaning.
"""

from enum import IntEnum, IntFlag, unique
from typing import Optional, Union

# import logging
#
# LOGGER = logging.getLogger(__name__)

XCP_PROTOCOL_VERSION = 1


class SessionStatus(IntFlag):
    StoreCalReq = 1
    StoreDaqReq = 4
    ClearDaqReq = 8
    DaqRunning = 0x40
    Resume = 0x80


class ProtectionStatus(IntFlag):
    CalibrationAndPagingIsProtected = 1
    DaqIsProtected = 4
    StimIsProtected = 8
    ProgrammingIsProtected = 0x10


class ResourceFlag(IntFlag):
    CalibrationAndPagingSupported = 1
    DaqSupported = 4
    StimSupported = 8
    ProgrammingSupported = 16


class ComModeBasicFlag(IntFlag):
    MSBFirst = 1
    AddressGranularity0 = 2
    AddressGranularity1 = 4
    SlaveBlockModeAvailable = 64
    MoreTypesAvailable = 128


class ComModeOptional(IntFlag):
    MasterBlockMode = 1
    InterleavedMode = 2


class Granularity(IntEnum):
    """
    A local / non-protocol enum for convenience
    may be removed later if a better solution presents itself.
    """
    Byte = 0
    Word = 1
    DoubleWord = 2
    Reserved = 3


@unique
class ErrCode(IntEnum):
    CmdSync = 0  # Not an Error

    CmdBusy = 0x10
    DaqActive = 0x11
    PgmActive = 0x12

    CmdUnknown = 0x20
    CmdSyntax = 0x21
    OutOfRange = 0x22
    WriteProtected = 0x23
    AccessDenied = 0x24
    AccessLocked = 0x25
    PageNotValid = 0x26
    ModeNotValid = 0x27
    SegmentNotValid = 0x28
    Sequence = 0x29
    DaqConfig = 0x2A

    MemoryOverflow = 0x30
    Generic = 0x31
    Verify = 0x32


ERR_CODE_SEVERITY = {
    ErrCode.CmdSync: 0,
    ErrCode.CmdBusy: 2,
    ErrCode.DaqActive: 2,
    ErrCode.PgmActive: 2,
    ErrCode.CmdUnknown: 2,
    ErrCode.CmdSyntax: 2,
    ErrCode.OutOfRange: 2,
    ErrCode.WriteProtected: 2,
    ErrCode.AccessDenied: 2,
    ErrCode.AccessLocked: 2,
    ErrCode.PageNotValid: 2,
    ErrCode.ModeNotValid: 2,
    ErrCode.SegmentNotValid: 2,
    ErrCode.Sequence: 2,
    ErrCode.DaqConfig: 2,
    ErrCode.MemoryOverflow: 2,
    ErrCode.Generic: 2,
    ErrCode.Verify: 3
}


def get_severity_by_err_code(error_code: ErrCode) -> Optional[int]:
    return ERR_CODE_SEVERITY.get(error_code)


@unique
class EvCode(IntEnum):
    ResumeMode = 0  # Slave starting in RESUME mode
    ClearDAQ = 1  # DAQ conf in NvM is cleared
    StoreDAW = 2  # DAQ conf stored in NvM
    StoreCAL = 3  # CAL stored in NvM
    CmdPending = 5  # Slave requests restart timeout
    DAQOverload = 6  # DAQ processor overload
    SessionTerminated = 7  # Session terminated by slave device
    User = 0xFE  # User defined event
    Transport = 0xFF  # Transport layer specific event


EV_CODE_SEVERITY = {
    EvCode.ResumeMode: 0,
    EvCode.ClearDAQ: 0,
    EvCode.StoreDAW: 0,
    EvCode.StoreCAL: 0,
    EvCode.CmdPending: 1,
    EvCode.DAQOverload: 1,
    EvCode.SessionTerminated: 3,
    EvCode.User: 0,
}


def get_severity_by_ev_code(ev_code: EvCode) -> Optional[int]:
    return EV_CODE_SEVERITY.get(ev_code)


class ConnectMode(IntEnum):
    Normal = 0
    User = 1


class ServCodes(IntEnum):
    Reset = 0
    Text = 1


@unique
class StdCmd(IntEnum):
    Connect = 0xFF
    Disconnect = 0xFE
    GetStatus = 0xFD
    Sync = 0xFC

    GetCommModeInfo = 0xFB
    GetId = 0xFA
    SetRequest = 0xF9
    GetSeed = 0xF8
    Unlock = 0xF7
    SetMta = 0xF6
    Upload = 0xF5
    ShortUpload = 0xF4
    BuildChecksum = 0xF3
    TransportLayerCmd = 0xF2
    UserCmd = 0xF1

    Download = 0xF0
    DownloadNext = 0xEF
    DownloadMax = 0xEE
    ShortDownload = 0xED
    ModifyBits = 0xEC

    SetCalPage = 0xEB
    GetCalPage = 0xEA

    GetPagProcessorInfo = 0xE9
    GetSegmentInfo = 0xE8
    GetPageInfo = 0xE7
    SetSegmentMode = 0xE6
    GetSegmentMode = 0xE5
    CopyCalPage = 0xE4

    ClearDaqList = 0xE3
    SetDaqPtr = 0xE2
    WriteDaq = 0xE1
    SetDaqListMode = 0xE0
    GetDaqListMode = 0xDF
    StartStopDaqList = 0xDE
    StartStopSync = 0xDD

    GetDaqClock = 0xDC
    ReadDaq = 0xDB


@unique
class PacketIdFromServer(IntEnum):
    Response = 0xFF
    Error = 0xFE
    Event = 0xFD
    ServiceRequest = 0xFC


def parse_connect_response(data: bytes, endianess: str) -> dict:
    """
    Parse the connect response data.

    :param data: The response data.
    :type data: bytes
    :param endianess: The endianess.
    :type endianess: str
    :return: The contents as a dictionary.
    :rtype dict
    """
    resource, com_mode_basic, max_cto = data[0:3]
    resource_flags = ResourceFlag(resource)
    com_mode_basic_flags = ComModeBasicFlag(com_mode_basic)
    granularity = Granularity((com_mode_basic >> 1) & 0x3)
    max_dto = int.from_bytes(data[3:5], "big")
    protocol_layer_version, transport_layer_version = data[5:7]

    return {"resource_flags": resource_flags,
            "com_mode_basic_flags": com_mode_basic_flags,
            "granularity": granularity,
            "max_cto": max_cto,
            "max_dto": max_dto,
            "protocol_layer_version": protocol_layer_version,
            "transport_layer_version": transport_layer_version
            }


def parse_get_status_response(data: Union[bytes, bytearray], endianess: str) -> dict:
    """
    Parse the get status response data.

    :param data: The response data.
    :type data: bytes
    :param endianess: The endianess.
    :type endianess: str
    :return: The contents as a dictionary.
    :rtype dict
    """
    return dict(session_status=SessionStatus(data[0]),
                protection_status=ProtectionStatus(data[1]),
                session_config_id=int.from_bytes(data[3:5], endianess))


def parse_get_comm_mode_info(data: Union[bytes, bytearray], endianess: str) -> dict:
    """
    Parse the get status response data.

    :param data: The response data.
    :type data: bytes
    :param endianess: The endianess.
    :type endianess: str
    :return: The contents as a dictionary.
    :rtype dict
    """

    return dict(comm_mode_optional=ComModeOptional(data[1]),
                max_bs=data[3],
                min_st=data[4] / 10000,
                queue_size=data[5],
                xcp_driver_version=float("{0}.{1}".format(data[6] >> 4, data[6] & 0xF)),
                )


CMD_TO_RESPONSE_PARSER_MAPPING = {
    StdCmd.Connect: parse_connect_response,
    StdCmd.GetStatus: parse_get_status_response,
    StdCmd.GetCommModeInfo: parse_get_comm_mode_info,
}


def parse_response_data(cmd: StdCmd, data: bytes, endianess: str) -> dict:
    """
    Parse the response data and call the appropriate sub parser.

    :param cmd: The command which this response is for.
    :type cmd: StdCmd
    :param data: The response data.
    :type data: bytes
    :param endianess: The endianess.
    :type endianess: str
    :return: The contents as a dictionary.
    :rtype dict
    """
    parser = CMD_TO_RESPONSE_PARSER_MAPPING.get(cmd)
    ret = {}
    if parser is not None and callable(parser):
        ret.update(parser(data=data,
                          endianess=endianess))
    # else:
    #     LOGGER.error("No parser for {0}".format(cmd.name))
    return ret


def parse_response_packet(data: bytes) -> dict:
    """
    Parse a response packet.

    :param data: The packet data.
    :type data: bytes
    :return: A dictionary with the values.
    :rtype: dict
    """
    ret = dict(command_response_data=data[1:])
    return ret


def parse_error_packet(data: bytes) -> dict:
    """
    Parse an error packet.

    :param data: The packet data.
    :type data: bytes
    :return: A dictionary with the values.
    :rtype: dict
    """
    error_code = ErrCode(data[1])
    ret = dict(error_code=error_code,
               severety=get_severity_by_err_code(error_code=error_code),
               optional=data[2:])
    return ret


def parse_event_packet(data: bytes) -> dict:
    """
    Parse an event packet.

    :param data: The packet data.
    :type data: bytes
    :return: A dictionary with the values.
    :rtype: dict
    """
    ev_code = EvCode(data[1])
    ret = dict(ev_code=ev_code,
               severety=get_severity_by_ev_code(ev_code=ev_code),
               optional=data[2:])
    return ret


def parse_service_packet(data: bytes) -> dict:
    """
    Parse a service packet.

    :param data: The packet data.
    :type data: bytes
    :return: A dictionary with the values.
    :rtype: dict
    """
    ret = dict(serv_code=ServCodes(data[1]),
               optional=data[2:])
    return ret


SERVER_PACKET_ID_TO_PARSER_MAPPING = {
    PacketIdFromServer.Response: parse_response_packet,
    PacketIdFromServer.Error: parse_error_packet,
    PacketIdFromServer.Event: parse_event_packet,
    PacketIdFromServer.ServiceRequest: parse_service_packet
}


def parse_packet_from_server(data: Union[bytes, bytearray]) -> dict:
    """
    Parse a packet from the server.

    :param data: The message data.
    :type data: bytes, bytearray
    :return: A dictionary.
    :rtype: dict
    """
    ret = {}
    try:
        packet_id = PacketIdFromServer(data[0])
    except ValueError:
        # likely a daq packet
        pass
    else:
        ret.update({"packet_id": packet_id})
        parser = SERVER_PACKET_ID_TO_PARSER_MAPPING.get(packet_id)
        if parser is not None and callable(parser):
            ret.update(parser(data=data))
        # else:
        #     LOGGER.error("No parser for {0}".format(packet_id.name))
    return ret


def concat_connect_command(mode: ConnectMode = ConnectMode.Normal) -> bytes:
    """
    Concat the connect command message.

    :param mode: The defined Mode
    :type mode: ConnectMode
    :return: The message bytes.
    :type: bytes
    """
    return bytes((StdCmd.Connect, mode))


def parse_connect_command(data: bytes) -> dict:
    """
    Parse a connect command message

    :param data: The data bytes.
    :type data: bytes
    :return: A dictionary.
    :rtype: dict(pid=StdCmd, mode=ConnectMode)
    """
    return dict(pid=StdCmd(data[0]), mode=ConnectMode(data[1]))


PACKET_ID_TO_PARSER_MAPPING = {
    StdCmd.Connect: parse_connect_command
}


def parse_packet_from_client(data: Union[bytes, bytearray]) -> dict:
    """
    Parse a command message from client to server.

    :param data: The message data.
    :type data: bytes, bytearray
    :return: A dictionary.
    :rtype: dict
    """
    packet_id = StdCmd(data[0])
    parser = PACKET_ID_TO_PARSER_MAPPING.get(packet_id)
    ret = {"packet_id": packet_id}
    if parser is not None and callable(parser):
        ret.update(parser(data=data))
    # else:
    #     LOGGER.error("No parser for {0}".format(packet_id.name))
    return ret


def concat_response_packet(command_response_data: Optional[Union[bytes, bytearray]] = None) -> bytearray:
    """
    Concat the response packet

    :param command_response_data: The
    :return:
    """
    ret = bytearray((PacketIdFromServer.Response,))
    if command_response_data is not None:
        ret.extend(command_response_data)
    return ret


def concat_connect_response(resource: ResourceFlag,
                            com_mode_basic: ComModeBasicFlag,
                            max_cto: int,
                            max_dto: int,
                            protocol_layer_version: int = 1,
                            transport_layer_version: int = 1,
                            ) -> bytes:
    """
    Concat the connect response message.

    :param resource: The resource flags.
    :type resource: ResourceFlag
    :param com_mode_basic: The com mode basic flags.
    :type com_mode_basic: ComModeBasicFlag
    :param max_cto: Max bytes of command transfer object (CTO)
    :type max_cto: int
    :param max_dto: Max bytes of data transfer object (DTO)
    :type max_dto: int
    :param protocol_layer_version: Protocol Major Version
    :type protocol_layer_version: int
    :param transport_layer_version: Transport Layer Major Version
    :type transport_layer_version: int
    :return: The message as bytes.
    :rtype: bytes
    """
    data = bytearray((resource, com_mode_basic, max_cto))
    data.extend(max_dto.to_bytes(2, "big"))
    data.extend((protocol_layer_version, transport_layer_version))
    return bytes(data)


def concat_disconnect_command() -> bytes:
    """
    Concat the connect command.

    :return: The message as bytes.
    :rtype: bytes
    """
    return bytes((StdCmd.Disconnect,))


def concat_get_status_command() -> bytes:
    """
    Concat the get status command.

    :return: The message as bytes.
    :rtype: bytes
    """
    return bytes((StdCmd.GetStatus,))


def concat_status_response(session_status: SessionStatus,
                           resource_protection_status: ProtectionStatus,
                           session_config_id: int,
                           endianess: str = "big") -> bytes:
    """
    Concat the response to get_status() command.

    :param session_status: The session status.
    :type session_status: SessionStatus
    :param resource_protection_status: The resource protection status.
    :type resource_protection_status: ProtectionStatus
    :param session_config_id: The session configuration id.
    :type session_config_id: int
    :param endianess: The endianess big or little.
    :type endianess: str
    :return: The message as bytes.
    :rtype: bytes
    """
    ret = bytearray((session_status, resource_protection_status, 0))
    ret.extend(session_config_id.to_bytes(2, endianess))
    return ret


def concat_get_comm_mode_info() -> bytes:
    """
    Concat the get comm mode info command.

    :return: The message as bytes.
    :rtype: bytes
    """
    return bytes((StdCmd.GetCommModeInfo,))


def concat_comm_mode_info_response(comm_mode_optional: ComModeOptional,
                                   max_bs: int,
                                   min_st: float,
                                   queue_size: int,
                                   xcp_driver_version: float,
                                   ) -> bytes:
    """
    Concat the response to get_com_mode_info() command.

    :param comm_mode_optional: Optional Com Mode Flags
    :type comm_mode_optional: ComModeOptional,
    :param max_bs: Max block size.
    :type max_bs: int
    :param min_st: Minimal separation time between packets in seconds(float). This is converted to 100us steps.
    :type min_st: float
    :param queue_size: Size of rx message queue in Server
    :type queue_size: int
    :param xcp_driver_version: The version number of xcp driver.
                               In Protocol this shows up as High Nibble = Major Version / Low Nibble = Minor Version
    :type xcp_driver_version: float
    :return: The message as bytes.
    :rtype: bytes
    """
    formatted_min_st = min_st * 10000  # 1ms = 10
    xcp_driver_version_major = int(xcp_driver_version)
    xcp_driver_version_minor = int((xcp_driver_version - xcp_driver_version_major) * 10)
    formatted_xcp_driver_version = ((xcp_driver_version_major << 4) | xcp_driver_version_minor)
    return bytes((0, comm_mode_optional, 0, max_bs, formatted_min_st, queue_size,
                  formatted_xcp_driver_version))
