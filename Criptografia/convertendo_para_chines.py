def esconde(msg):
    s = ""
    for c in msg: s += chr(ord(c)+30000)
    return s

def mostra(msg):
    s = ""
    for c in msg: s += chr(ord(c) - 30000)
    return s


if __name__ == "__main__":
    palavra = input("Digite uma frase: ")
    a = esconde(palavra)
    b = mostra(a)
    print(a)
    print(b)