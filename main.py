import os
import time
notas={}
def adiciona():
  while True:
    aln=input("digite seu nome: ")
    if notas.get(aln):
        print("ja existe o aluno")
    else:
      prof=float(input("digite sua nota: "))
      x=input("deseja adiciona mais algum aluno? ")
      notas[aln]=prof
      if x=="s":
        continue
      elif x=='n':
        menu()
def alterar():
  x = input("qual nome deseja alterar: ")

  if notas.get(x):
    nota=float(input("digite a nova nota: "))
    notas[x]=nota
    menu()
  else:
    print("não existe esse aluno!!")
    time.sleep(5)
    menu()
def excluir():
  e=input("qual nome deseja excluir: ")
  if notas.get(e):
    notas.pop(e)
    menu()
  else:
    print("nao existe")
    time.sleep(5)
    menu()

def mostrar():
  print (notas)
  time.sleep(5)
  menu()
def fim():
  print ("obgd, volte sempre :)")

def menu():
  os.system('clear')
  d=int(input("1- para adicionar algum aluno \n2- para alterar \n3- para excluir uma nota \n4- para saber a lista \n5- para Sair \n"))
  if d==1:
    adiciona()
  elif d==2:
    alterar()
  elif d==3:
    excluir()
  elif d==4:
    mostrar()
  elif d==5:
    fim()

menu()