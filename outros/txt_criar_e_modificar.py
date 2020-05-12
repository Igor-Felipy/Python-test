#como criar e modificar arquivos:

'''
'r'  -> usado somente para ler algo
'w'  -> usado somente para escrever algo
'r+' -> usado para ler e escrever algo
'a'  -> usado para acrescentar algo
'''

valores_celulares = [850, 2230, 1500, 3500, 5000]

'''
with open('valores_celulares.txt','w') as arquivo:
    for valor in valores_celulares:
        arquivo.write(str(valor) + )
'''
'''
with open('valores_celulares.txt','r') as arquivo:
    for valor in valores_celulares:
        print(valor)
'''
'''
with open('valores_celulares.txt','r') as arquivo:
    for valor in arquivo:
        print(valor) 
'''
with open('valores_celulares.txt','r+') as arquivo:
    for valor in arquivo:
        print(valor)
    arquivo.write('9000')