import hashlib
from operator import xor


m = "Um HMAC gera tags para etiquetar mensagens"
expected0="821f34c9796e35312d3c19a40edc64860c7ea9b8ce636be95c2287a233c8b343"
expected997="94c18514b5a01471d05945157d78fabe3eaf4e5f7ef9b4240a244308c5213654"
opad = 0x5C
ipad = 0x36

#k = 0x00BB
k = 0

sha256_1 = hashlib.sha256()
sha256_2 = hashlib.sha256()


a = bytes(xor(k, opad))

b_1 = bytes(xor(k, ipad))
b_2 = b_1 + m.encode()

sha256_1.update(b_2)
b = sha256_1.digest()


c = a + b
sha256_2.update(c)
myHMAC = sha256_2.hexdigest()

print("my:\t" + myHMAC)
print("k=0:\t" + expected0)
print("k=997:\t" + expected997)