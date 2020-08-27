#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
while True:
    nota = int(input("entre com a nota: "))
    if nota <= 10 and nota >= 0 :
        break 
    else:
        print("Nota errada, tente denovo! \n")
        continue