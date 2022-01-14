import fastcrc
import struct

string = b'1AC9'.decode()
print(f'str: {string}')
ascii = [ord(c) for c in string]
print(f'ascii: {ascii}')
ascii_d = [c-0x30 if c<0x40 else c-0x37 for c in ascii]
print(f'decimal: {ascii_d}')
binary = ''.join([format(d, '04b') for d in ascii_d])
print(f'binary: {binary}')
decimal = int(binary, 2)
print(f'decimal: {decimal}')


