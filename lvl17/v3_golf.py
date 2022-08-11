def t(c,d):return c+len(d).to_bytes(4,"big")+d
r=range
def encode(b):a=bytes(r(97,123));n=[i for i in r(2,8000) if all(i%p for p in r(2,i))];return bytes([z^(x&255) for z,x in zip(t(b"BEGN",a)+t(b"DATA",b)+t(b"END.",a.upper()),n)])
