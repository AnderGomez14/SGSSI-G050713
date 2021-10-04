import hashlib, sys

def tarea1():
    input = "SGSSI-21.CB.01.txt"
    with open(input, "rb") as f:
        bytes = f.read()
        hash = hashlib.sha256(bytes).hexdigest()
        print("El hash del fichero "+input+" es: "+hash)

def tarea2():
    input = "SGSSI-21.CB.01.txt"
    output = "SGSSI-21.CB.01_output.txt"
    with open(input, "rb") as f:
        bytes = f.read()
        hash = hashlib.sha256(bytes).hexdigest()
    f = open(output, "wb")
    f.write(bytes + str.encode(hash))
    f.close()


def tarea3():
    input = "SGSSI-21.CB.01.txt"
    output = "SGSSI-21.CB.01_output.txt"
    with open(input, "rb") as f:
        bytes = f.read()
        hash_input = hashlib.sha256(bytes).hexdigest()
        print(len(bytes))
    with open(output, "rb") as f:
        bytes = f.read()
        hash_output = hashlib.sha256(bytes[:len(bytes)-64]).hexdigest()
        hash_guardado = bytes[len(bytes)-64:].decode()
        print(len(bytes))

    if(hash_input == hash_guardado == hash_output):
        print("El fichero esta correctamente firmado")
        print("hash_input: " + hash_input)
        print("hash_output: " + hash_output)
        print("hash_guardado: " + hash_guardado)
    else:
        print("Houston, tenemos un problema")
        print("hash_input: " + hash_input)
        print("hash_output: " + hash_output)
        print("hash_guardado: " + hash_guardado)

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



