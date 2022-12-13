import random

try:
    length = int(input("enter the length of password:"))
except:
    print("bad input")

chars = [*"1234567890-=!@#$%&*()_+`~qwertyuiopQWERTYUIOPasdfghjklASDFGHJKL:;'\"[]\\{}|zxcvbnm,./ZXCVBNM<>?"]
out = ""
for _ in range(length):
    random.shuffle(chars)
    out += chars[0]

print("random password:", out)