import hashlib
import sys
import os.path


def prefix(s1, s2):
    i = 0
    while True:
        if i < len(s1) and i < len(s2) and s1[i] == s2[i]:
            i = i+1
        else:
            break
    return i


def hash(n):
    if n == -1:
        return "0000000000000000000000000000000000000000000000000000000000000000"
    else:
        try:
            filename = "SGSSI-21.CB."+str(n).zfill(2)+".txt"
            with open(filename, "rb") as f:
                bytes = f.read()
                return hashlib.sha256(bytes).hexdigest()
        except:
            return ""


def parseBlock(n):
    filename = "SGSSI-21.CB."+str(n).zfill(2)+".txt"
    try:
        with open(filename, "r") as file:
            id_block = file.readline().replace("\n", "")

            line = file.readline().replace("\n", "")
            trabajo = line.split()[0]
            data_lines = line.split()[1]

            previus_block = file.readline().replace("\n", "")

            data = file.readlines()
            data = [d.replace("\n", "") for d in data]
            data = ' '.join(data).split()

            if(n > 2):
                nonce = data[len(data)-1]
                data.pop()

            if(int(data_lines) != len(data)):
                return 1
            elif(int(id_block) != n):
                return 2
            elif(previus_block != hash(n-1)):
                return 3
            elif(n > 2 and prefix(hash(n), "00000") < 5):
                return 4
            else:
                return 0
    except Exception as E:
        print(E)
        return -1


def checkBlockChain():
    n = 0
    error = 0
    while True:
        if os.path.exists("SGSSI-21.CB."+str(n).zfill(2)+".txt"):
            error = parseBlock(n)
            if error != 0:
                break
        else:
            break
        n = n+1
    return errorManagement(error, n, "all")


def errorManagement(error, n, tipo):
    if n == 0 and error == 0 and tipo == "all":
        print("ERROR: No se encuentra la cadena de bloques.")
        return False
    if error == 0 and tipo == "all":
        print("La cadena de bloques tiene " +
              str(n) + " bloques y todos son validos.")
        return True
    if error == 0 and tipo == "cb":
        print("El bloque " + str(n) + " es valido.")
        return True
    if error == -1:
        print("ERROR (Bloque "+str(n) +
              "): Bloque no encontrado")
        return False
    if error == 1:
        print("ERROR (Bloque "+str(n) +
              "): El numero de datos introducidos no es correcto.")
        return False
    if error == 2:
        print(
            "ERROR (Bloque "+str(n) +
            "): El numero del bloque en el nombre del fichero y en el fichero no coinciden.")
        return False
    if error == 3:
        print("ERROR (Bloque "+str(n) +
              "): El hash del bloque anterior y el guardado no coinciden")
        return False
    if error == 4:
        print("ERROR (Bloque "+str(n) +
              "): El hash del bloque no comienza por 5 ceros")
        return False
    else:
        print("ERROR (Bloque "+str(n) +
              "): Desconocido")
        return False


if __name__ == "__main__":
    if(len(sys.argv) > 1):
        if(sys.argv[1] == "-cb" or sys.argv[1] == "-check_block"):
            if(len(sys.argv) > 2):
                errorManagement(parseBlock(
                    int(sys.argv[2])), sys.argv[2], "cb")
            else:
                print("Falta el numero del bloque: -cb XX")
        elif(sys.argv[1] == "-all" or sys.argv[1] == "-check_blockchain"):
            checkBlockChain()
        else:
            print("Comando no encontrado")
    else:
        checkBlockChain()  # Debug only
        print("Introduce un comando")
