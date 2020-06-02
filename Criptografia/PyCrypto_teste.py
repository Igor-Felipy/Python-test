from Crypto.Cipher import AES

frase = input("Entre com alguma coisa para ver a criptografia AES ")
chave = input("Entre com uma chave de Criptografia ")

encryption_suite = AES.new(chave, AES.MODE_CBC)
cifrar = encryption_suite.encrypt(frase)

print(f"Sua chave é {chave}")

print(cifrar)

decryption_suite = AES.new(chave, AES.MODE_CBC)
descifrado = decryption_suite.decrypt(cifrar)

print(descifrado)