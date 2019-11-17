import struct
from enum_operation_code import Operation_Code

# unsigned char (operation code), unsigned int (page id), unsigned int (page size), pending data
INITIAL_FORMAT_INTERFACE = 'BII'
INITIAL_FORMAT_LOCAL = 'BB'

def create_packet_to_distributed_interface(operation_code, page_id, data):

    data_size = len(data)
    packet_format = get_format(INITIAL_FORMAT_INTERFACE, data_size)

    return struct.pack(packet_format, operation_code, page_id, data_size, data)

def create_packet_to_local(operation_code, page_id, data):

    # If it's LOAD, it needs to return the data page.
    if(operation_code == Operation_Code.LOAD.value):

        data_size = len(data)
        packet_format = get_format(INITIAL_FORMAT_LOCAL, data_size)
        return struct.pack(packet_format, operation_code, page_id, data)
    else:
        # Only confirmation or error.
        return struct.pack(INITIAL_FORMAT_LOCAL, operation_code, page_id)


def get_format(INITIAL_FORMAT, size):
    return INITIAL_FORMAT + str(size) + 's'
