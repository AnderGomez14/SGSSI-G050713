import hashlib
import sys
import time
import secrets


def tarea1():
    input = "SGSSI-21.CB.04.txt"
    with open(input, "rb") as f:
        bytes_file = f.read()
    cont = 0
    while True:
        hash_i = secrets.token_hex(nbytes=4)
        hash = hashlib.sha256(bytes_file + str.encode(hash_i)).hexdigest()
        if hash.startswith('0000000'):
            break
        cont += 1

    output = "SGSSI-21.CB.04_mined.txt"
    f = open(output, "wb")
    f.write(bytes_file + str.encode(hash_i))
    f.close()
    print(cont)


tarea1()
