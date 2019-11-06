import hashlib

t = hashlib.md5()
t.update(b"zoushqing")
t.hexdigest()  # '018754be1f9e63e754bf1d117cf6c4f3'------无论是什么加密  总是32位的 值
