from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

flag = open("flag.txt", "rb").read()
key = pad(os.urandom(1), 16)

c = AES.new(key, AES.MODE_ECB)
print(c.encrypt(pad(flag,16)))

#cipher text : b'\xaa%\xef\xd4\x13\xd88\x02\xf72\x89[\x12\xc4/\xe5?\xb3)\xde\x08:\xd7L\xdbf\x8c$)\xb6\xd6\x8b\xc2^\xa2\x0bQ\xb2d\xf58\xd0\xa68\r\xcef\x17'
