import hashlib
import sys
import time
import secrets


def mine(input, output, id, numceros):
    with open(input, "rb") as f:
        bytes_file = f.read()
    cont = 0
    prefijo = "0"*int(numceros)
    while True:
        hash_i = secrets.token_hex(nbytes=4) + " " + id
        hash = hashlib.sha256(bytes_file + str.encode(hash_i)).hexdigest()
        if hash.startswith(prefijo):
            break
        cont += 1

    f = open(output, "wb")
    f.write(bytes_file + str.encode(hash_i))
    f.close()
    print(cont)


if __name__ == '__main__':
    if(len(sys.argv) == 1 or sys.argv[1] == "-h"):
        print("Uso: python mine.py archivo_entrada archivo_salida id num_ceros")
    elif(len(sys.argv) > 4):
        mine(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("Numero de argumentos incorrecto")
