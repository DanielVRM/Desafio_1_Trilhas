import requests

#importando txts do github
regras_dados = requests.get('https://raw.githubusercontent.com/YammaTM/Desafio_txts/main/sum_regras.txt')

niveis_dados = requests.get('https://raw.githubusercontent.com/YammaTM/Desafio_txts/main/sum_niveis.txt')

classes_dados = requests.get('https://raw.githubusercontent.com/YammaTM/Desafio_txts/main/sum_classes.txt')

atributos_dados = requests.get('https://raw.githubusercontent.com/YammaTM/Desafio_txts/main/z_sum_atributos.txt')

tipos_dados = requests.get('https://raw.githubusercontent.com/YammaTM/Desafio_txts/main/z_sum_tipos.txt')

#Funções
def organiza_em_tupla(lista):
  tupla = []
  i = 0
  while i <= len(lista)-1:
    tupla.append((lista[i],lista[i+1]))
    i += 2
  return tupla

def separa_dados(texto):
  texto = texto.replace('\r\n','')
  texto_separado = texto.split('!')
  texto_separado = organiza_em_tupla(texto_separado)
  return texto_separado

#Menu_lista_0
start = ['Regras', 'Níveis de Monstros', 'Classes de Monstros', 'Atributos de Monstros', 'Tipos de Cartas']

#Distribuindo dados para a superlist
regras_dados = regras_dados.text
regras = separa_dados(regras_dados)

niveis_dados = niveis_dados.text
niveis = separa_dados(niveis_dados)

classes_dados = classes_dados.text
classes = separa_dados(classes_dados)

atributos_dados = atributos_dados.text
atributos = separa_dados(atributos_dados)

tipos_dados = tipos_dados.text
tipos = separa_dados(tipos_dados)

superlist = [regras, niveis, classes, atributos, tipos]

from IPython.display import clear_output

def menu(lista,camada):
  clear_output()
  for item in lista:
    if camada == 0:
      print(f'{lista.index(item)+ 1} - {item}\n') #print dos elementos da lista
    else:
      print(f'{lista.index(item)+ 1} - {item[0]}\n') #print dos elementos caso estejam organizados dentro de outra lista
  print('\n\n0 - Sair')
  return input('\nDigite seu comando: ')

def condicao(lista,lista0,camada,controle):
  if camada == 0:
    op = menu(lista0,camada)
  else:
    op = menu(lista,camada)

  n = int(op) - 1 #utilização de variável para transformar o input do usuário em inteiro, pois a última é tratada como string e servirá como comparação nas condições
  controle.append(n)
  while(op):
    if n < len(lista) and n > -1 and camada == 0:
      camada += 1 
      condicao(lista[n],lista0,camada,controle)
      break
      
    elif n <len(lista) and n > -1:
      print(lista[controle[camada]][1])
      camada += 1
      break

    elif op == "0":
      break

    elif op !="":
      print("\n Opcao invalida, tente novamente")
      break

camada = 0

controle = []

condicao(superlist, start, camada, controle)