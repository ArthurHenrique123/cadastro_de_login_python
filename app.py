import PySimpleGUI as sg
from time import sleep #permite pausar a execução

sg.theme('reddit')

#layout
tela_login = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Seha')],
    [sg.Input(password_char='*',key='senha')],
    [sg.Button('Enviar')],
    [sg.Output(size=(43,10))]
]

# criando a janela 
janela = sg.Window('Login', layout=tela_login)
# ler os eventos 
while True:
    event,values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    #VERIFICAR SE O USUARIOS E SENHAS ESTÃO CADASTRADOS!
    elif event == 'Enviar':
       usuairo_digitados =  values['usuario']
       senha_digitada = values["senha"]
       print('O passo 1... Executado com sucesso!')
       sleep(5)
       print('O passo 2...Executado com sucesso!')
       sleep(6)
       print("O passo 3... Feito")