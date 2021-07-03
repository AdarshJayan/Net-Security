


import hashlib,binascii

# for mp5

c = hashlib.md5()
c.update(b"AdarshJayan")
print("Hashed password for md5:")
print(c.hexdigest())

# for 3 other algorithms

c = hashlib.sha256()
c.update(b"HelloWorld")
print(" \n Hashed password for sha256:")

print(c.hexdigest())
c = hashlib.sha1()
c.update(b"Coimbatore")
print("\n Hashed password for sha1:")

print(c.hexdigest())
c = hashlib.sha512()
c.update(b"Pune")
print(" \n Hashed password for sha512:")

print(c.hexdigest())

# Salting and Iteration

c = hashlib.pbkdf2_hmac("md5", b"AdarshJayan",b"shimla",10)
print(" \n Salted and iterated password is :")

print(binascii.hexlify(c))
 # ShapeAI the salting  function was already inbuilt so I used it...:)



