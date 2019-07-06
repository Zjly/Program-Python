import hashlib

s = ''
# s.encode()#变成bytes类型才能加密
m = hashlib.md5(s.encode())
print(m.hexdigest())

m = hashlib.sha3_224(s.encode())  # 长度是224
print(m.hexdigest())

m = hashlib.sha3_256(s.encode())  # 长度是256
print(m.hexdigest())

m = hashlib.sha3_512(s.encode())  # 长度是512
print(m.hexdigest())
