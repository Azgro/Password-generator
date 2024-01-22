import string as st
import random
import PySimpleGUI as sg
import os
from playsound import playsound

letras = st.ascii_letters
num = st.digits
especial = st.punctuation
algoritmo = letras + num + especial

class PassGen:
    def __init__(self):
        sg.theme('Black')
        playsound('sound.mp3', block=False)
        layout = [
            [sg.Text('Site/Software', size=(10, 1)),
             sg.Input(key='site', size=(20, 1))],
            [sg.Text('E-mail/User', size=(10, 1)),
             sg.Input(key="user", size=(20, 1))],
            [sg.Text('Quantidade de Caracteres'),
             sg.Combo(values=list(range(30)), key='total_chars', default_value=1, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha')]
        ]

        self.janela = sg.Window('Gerador de senha', layout)

    def iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WIN_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha, valores)

    def gerar_senha(self, valores):
        char_list = algoritmo
        chars = random.choices(char_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass

    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(f'site: {valores["site"]}, usuario: {valores["user"]}, nova senha: {nova_senha}\n')

        print('Arquivo salvo')

gen = PassGen()
gen.iniciar()
