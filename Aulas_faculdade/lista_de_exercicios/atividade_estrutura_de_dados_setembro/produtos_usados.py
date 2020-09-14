# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 14:57:01 2020

@author: prof. Gregorio 
Disciplina: Estrutura de Dados
"""

"""
Integrantes do Grupo:
    RA     NomeCompleto (em Ordem Alfabética):
    250104 Aquiles Lopes de Oliveira
    111646 Edward Jun Ho Choi
    114137 Igor Felipy Lopes de França
    031717 Luccas Neves Palhares
    112133 Luiz Felipe Luna da Silva
    109464 Renan Monteiro Silva 
"""

PRODUTOS = "lista_produtos.txt"

def carregar():
    """ Retorna uma string dos produtos e seus preços no formato:
        produto1 preco1 produto2 preco2 ... produtoN precoN
    Todas os produtos estão escrito em letras minúsculas.
    O teste do programa será feito com um arquivo com dados diferentes """

    print("\nCarregando os produtos do arquivo...\n")
    
    # inFile: file
    inFile = open(PRODUTOS, 'r')
    
    # dados: string
    dados = inFile.readline()
    
    return dados

'''As linhas seguintes são para testes, podem ser comentadas para o programa final '''   
#prod = carregar()
#print(prod)

def lista_tupla(aLista):
    '''
    Parameters
    ----------
    aLista : lista com os produtos
        
    Returns
    -------
    Uma Tupla com os produtos no formato ( (<str>produto1, <int>valor1), (<str>produto1, <int>valor1), ... )
    '''
    tupla = ()
    l = []
    # Escreva seu código aqui
    lista = aLista.split(" ")
    for n in range(0,len(lista),2):
      b = tuple((lista[n],int(lista[n+1])))
      l.append(b)
    tupla = tuple(l)
    return tupla



def get_Produtos(aTupla):
    '''
    Parameters
    ----------
    aTupla : Uma Tupla com os produtos no formato
    ( (<str>produto1, <int>valor1), (<str>produto1, <int>valor1), ... )
        
    Returns
    -------
    uma tupla com 3 informações abaixo:
    1. O produto mais Barato (tupla): <produto> <valor>
    2. O produto mais caro   (tupla): <produto> <valor>
    3. Quantidade de Produtos Diferentes : <int>  
    '''
    tupla = ()
    # Escreva seu código aqui
    l = []
    barato = aTupla[0]
    caro = aTupla[0]


    for n in range(0,len(aTupla)):
      if barato[1] >= aTupla[n][1]:
        barato = aTupla[n]
      if caro[1] <= aTupla[n][1]:
        caro = aTupla[n]


    outra_lista = []
    for n in range(0,len(aTupla)):
      if not aTupla[n][0] in outra_lista:
        outra_lista.append(aTupla[n][0])
      else:
        pass
    
    qtd = len(outra_lista)

    l.append(barato)
    l.append(caro)
    l.append(qtd)
    tupla = tupla + tuple(l)
    return tupla



def main():
  produtos = carregar()
  tupla_fatiada = lista_tupla(produtos)
  prods = get_Produtos(tupla_fatiada)
  print(prods)

if __name__=="__main__":
  main()