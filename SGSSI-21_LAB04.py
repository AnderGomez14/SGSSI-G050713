import hashlib
import sys
import time
import secrets


def prefix(s1, s2):
    i = 0
    while True:
        if s1[i] == s2[i]:
            i = i+1
        else:
            break
    return i


i = 0
best_clash = ''
best_cont = 0


def tarea1():
    input = "SGSSI-21.CB.03.txt"
    with open(input, "rb") as f:
        bytes_file = f.read()
    i = 1
    while True:
        hash_i = secrets.token_hex(nbytes=4)
        hash = hashlib.sha256(bytes_file + str.encode(hash_i)).hexdigest()
        if hash[0] == '0':
            break
        i = i+1
    output = "SGSSI-21.CB.03_salida_tarea1.txt"
    f = open(output, "wb")
    f.write(bytes_file + str.encode(hash_i))
    f.close()
    print("Se han realizado " + str(i) + " iteraciones")


def tarea2():
    input = "SGSSI-21.CB.03.txt"
    with open(input, "rb") as f:
        bytes_file = f.read()
    i = 0
    best_cont = 0
    timeout = time.time() + 60
    while True:
        hash_i = secrets.token_hex(nbytes=4)
        hash = hashlib.sha256(bytes_file + str.encode(hash_i)).hexdigest()
        cont = prefix("000000000000000000000", hash)
        if cont > best_cont:
            best_clash = hash_i
            best_cont = cont
            print("Hash: " + str(hash) + " ; Cont: " + str(best_cont) +
                  " ; Iteracion: " + str(i))
        if (timeout <= time.time()):
            break
        i = i+1

    output = "SGSSI-21.CB.03_salida_tarea2.txt"
    f = open(output, "wb")
    f.write(bytes_file + str.encode(best_clash))
    f.close()
    print("Se han realizado " + str(i) + " iteraciones")


def tarea3():
    input = "SGSSI-21.CB.03.txt"
    with open(input, "rb") as f:
        bytes_file = f.read()
    i = 0
    best_cont = 0
    timeout = time.time() + 60
    while True:
        hash_i = secrets.token_hex(nbytes=4) + " G050713"
        hash = hashlib.sha256(bytes_file + str.encode(hash_i)).hexdigest()
        cont = prefix("000000000000000000000", hash)
        if cont > best_cont:
            best_clash = hash_i
            best_cont = cont
            print("Hash: " + str(hash) + " ; Cont: " + str(best_cont) +
                  " ; Iteracion: " + str(i))
        if (timeout <= time.time()):
            break
        i = i+1

    output = "SGSSI-21.CB.03_salida_tarea3.txt"
    f = open(output, "wb")
    f.write(bytes_file + str.encode(best_clash))
    f.close()
    print("Se han realizado " + str(i) + " iteraciones")


if __name__ == "__main__":
    if(len(sys.argv) > 1):
        if(sys.argv[1] == "-1"):
            tarea1()
        elif(sys.argv[1] == "-2"):
            tarea2()
        elif(sys.argv[1] == "-3"):
            tarea3()
        else:
            print("Comando incorrecto")
    else:
        print("Introduce un comando")
