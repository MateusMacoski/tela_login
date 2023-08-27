from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('DarkGrey6')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='Senha',password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
    # Janela
janela = sg.Window('Tela de Login', layout)

# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'mateus' and valores['Senha'] == 'abc': 
            print('Bem-vindo!')
