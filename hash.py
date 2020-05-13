import hashlib


print('''
MMM          MMM   DDDDDDDDD      555555555
MMMM        MMMM   DDD   DDDD     555
MMMMM      MMMMM   DDD    DDD     555
MMMMMM    MMMMMM   DDD    DDD     55555555
MMMMMMM  MMMMMMM   DDD    DDD           555
MMMMMMMMMMMMMMMM   DDD   DDDD           555
MMM          MMM   DDDDDDDDD      555555555       
''')
mystring = input('Enter string to hash: ')
hash_obj = hashlib.md5(mystring.encode())
print(hash_obj.hexdigest())
    