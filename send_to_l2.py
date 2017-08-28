import socket
import sys
'''
socket(AF_PACKET, SOCK_RAW, IPPROTO_RAW)
"lowpan0"
'''
ethframe = bytes([0x61, 0xcc, 0x1f, 0xcd, 0xab,
    
# Destination MAC addr
                #0xa8, 0x77, 0x17, 0xdb, 0x78, 0x47, 0x49, 0xfa,
                0x92, 0xb3, 0x8f, 0x47, 0x2f, 0xc1, 0x75, 0xd2,
                
# Source MAC addr
                0x0a, 0x08, 0xc2, 0xe7, 0xa2, 0x8c, 0x8f, 0xfe, 
                
# Other
                0x63, 0x00, 0x6a, 0x0a, 0xbc, 0xde, 0x3b,
                
# Source address
                0x0a, 0x08, 0xc2, 0xe7, 0xa2, 0x8c, 0x8f, 0xfc,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0xfe,
                
# Destination address
                #0xa8, 0x77, 0x17, 0xdb, 0x78, 0x47, 0x49, 0xf8,
                0x92, 0xb3, 0x8f, 0x47, 0x2f, 0xc1, 0x75, 0xd0,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0xfe,
                
                0x00, 0x01, 0x02, 0x03,
                0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x09, 0xec])
'''
ping_test = bytes([0x61, 0xcc, 0xf1, 0xcd, 0xab, 0xa8, 0x77, 0x17,
    0xdb, 0x78, 0x47, 0x49, 0xfa, 0xa0, 0x08, 0xc2, 0xe7, 0xa2, 0x8c, 0x8f, 0xfe,

    0x6a, 0x33, 0x0d, 0xef, 0xc2, 0x3a, 0x80, 0x00, 0xc3, 0x41,
    0x5e, 0x68, 0x00, 0x17, 0xf5, 0x3a, 0x65, 0x59, 0x00, 0x00, 0x00, 0x00,
    0x36, 0xd9, 0x05, 0x00, 0x00, 0x00, 0x00, 0x00, 0x10, 0x11, 0x12, 0x13,
    0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1a, 0x1b, 0x1c, 0x1d, 0x1e, 0x1f,
    0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2a, 0x2b,
    0x2c, 0x2d, 0x2e, 0x2f, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37])


0000   61 cc 00 cd ab a8 77 17 db 78 47 49 fa 0a 08 c2
0010   e7 a2 8c 8f fe 63 00 6a 0a bc de 3b 0a 08 c2 e7
0020   a2 8c 8f fc 00 00 00 00 00 00 80 fe a8 77 17 db
0030   78 47 49 f8 00 00 00 00 00 00 80 fe 00 01 02 03
0040   04 05 06 07 08 09 15 ec
'''

def sendRaw802154Frame(frame: bytearray, interface: str):
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
    s.bind((interface, 0))
    s.send(frame)

# If we are called directly, want to get byte array from stdin
# Note that we assume that the input is an ASCII array, and directly interpret
# each character as a byte
if __name__ == '__main__':
    sendRaw802154Frame(ethframe, "wpan0")
