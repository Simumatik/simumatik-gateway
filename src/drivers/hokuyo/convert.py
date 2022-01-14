import fastcrc

str = '1AC9'
print(f'str: {str}')
ascii = [ord(c) for c in str]
print(f'ascii: {ascii}')
ascii_d = [c-0x30 if c<0x40 else c-0x37 for c in ascii]
print(f'decimal: {ascii_d}')
binary = ''.join([format(d, '04b') for d in ascii_d])
print(f'binary: {binary}')
decimal = int(binary, 2)
print(f'decimal: {decimal}')
print(format(decimal, '04b'))
crc = fastcrc.crc16.kermit(b'000EVR00')
print(f'crc: {crc}')
