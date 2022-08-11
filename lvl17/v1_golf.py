import struct
def t(c,d):return c+struct.pack(">I",len(d))+d
def e(b):
 n=[2, 3]
 return [b[i]^(n[i] & 0xff) for i in range(len(b))]
def encode(i):
 a=b"abcdefghijklmnopqrstuvwxyz"
 return e(t(b"BEGN",a)+t(b"DATA",i)+t(b"END.",a.upper()))
