import pandas as pd
import re
import os
import smtplib
import openpyxl
import email
#import pywhatkit as kit
import pyautogui
from email.message import EmailMessage
from time import sleep


#validacao email destino ok
#metodo menu app
#cadastrar tarefas
#deletar tarefas
#visualizar tarefas
#criar planilha excel
#enviar email automaticamente
#enviar confirmacao via whpp


class Lista_de_tarefas:

    def iniciar(self):
        self.lista_tarefa = []
        #self.email_destino()
        self.menu()

    def email_destino(self):
        while True:
            self.email = str(input('Digite seu email: ')).lower()
            padrao_email = re.search(
                '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._-]+.[a-zA-Z]{2,}$',          #regex codigo de validacao de informacao
                self.email)
            if padrao_email:                       #/^[a-z0-9.]+@[a-z0-9]+\.[a-z]+\.([a-z]+)?$/i
                print('email valido!')
                break
            else:
                print('email invalido!')


    def menu(self):
        while True:
            menuprincipal = int(input('''
            MENU
            [1] Cadastrar
            [2] Visualizar
            [3] Deletar tarefas
            [4] Deletar no historico
            [5] Limpar historico
            [6]Sair
            opc: '''))

            match menuprincipal:                              #match nao funciona para teste, algo para escolha
                case 1: self.cadastrar()
                case 2: self.visualizar()
                case 3: self.deletar_tarefas()
                case 4: self.deletar_no_historico()
                case 5: self.limpar_historico()
                case 6: break
                case _: print('Opcao invalida')





    def cadastrar(self):
        while True:
            tarefa = str(input('Digite uma tarefa ou s para sair: ')).capitalize()

            if tarefa == 'S':
                break
            else:
                self.lista_tarefa.append(tarefa)

                try:
                    with open('src/tarefas/historico tarefas.txt', 'a',encoding='utf8') as arquivo:
                        arquivo.write(f'{tarefa}\n')

                except FileNotFoundError as e:
                    print(f'Erro: {e}')





    def visualizar(self):
        try:
            with open('src/tarefas/historico tarefas.txt','r',encoding='utf8') as arquivo:
                print(arquivo.read())

        except FileNotFoundError as e:
            print(f'Erro: {e}')




    def deletar_tarefas(self):
        for indice, item in enumerate(self.lista_tarefa,start=1):
            print(f'{indice} : {item}')
        while True:
            deletar = int(input('Digite a opçao: '))
            if deletar <= len(self.lista_tarefa):
                print(f'A tarefa {self.lista_tarefa[deletar-1]} foi removida com sucesso!')
                self.lista_tarefa.pop(deletar -1)
                break
            else:
                print('Opçao invalida!')




    def limpar_historico(self):
        try:

            with open('src/tarefas/historico tarefas.txt', 'w') as arquivo:
                arquivo.write('')

        except FileNotFoundError:
            print('Arquivo nao encontrado.')




    def deletar_no_historico(self):
        try:
            with open('src/tarefas/historico tarefas.txt', 'r') as arquivo:
                print(arquivo.read())

        except FileNotFoundError:
            print('Arquivo nao encontrado.')





start = Lista_de_tarefas()
start.iniciar()


