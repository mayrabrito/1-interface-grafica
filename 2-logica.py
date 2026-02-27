# Interface gráfica no Python
# Tkinter - vem com a instalação do interpretador do python
import tkinter as tk
from pathlib import Path

CORFUNDO = "#7DBBEB"
CORTEXTO = "#03182D"

def registar():
    nome = nome_entry.get()
    password = password_entry.get()

    if password == '' or nome == '':
        msg_label.configure(text='Por favor preencha os dados', fg="#bb3939")
    else:
        ficheiro = Path(r'dados.txt')

        with ficheiro.open('w', encoding='utf-8',errors='ignore') as file:
            file.write(f'NOME: {nome}\n')
            file.write(f'PASSWORD: {password}')
            msg_label.configure(tex='Dados Registados com Sucesso', fg="#39bb46")

# Criar a variável que representa a janela
root = tk.Tk()
root.configure(bg="#7DBBEB") # mudar cor do fundo da janela
root.title('1 - Esqueleto da GUI') #mudar título
root.geometry('600x400') # configura largura e altura
# root.state('zoomed') #inicia janela maximizada

# Para criar os elementos (widgets) há sempre 2 passos
# 1- Criar a variável que representa o widget
# tk.widget (qual janela?, qual texto?)
nome_label = tk.Label(root, text ='Digite o seu nome:',bg=CORFUNDO, fg=CORTEXTO, font=("Arial", 14, 'bold'))
# 2- Posicionar o widget na janela
nome_label.pack(pady=20) #sem o .pack não aparece. 

nome_entry = tk.Entry(root, width=30) #esse 30 refere-se a 30% do ecrã
nome_entry.pack() #colocar o .pack para aparecer

#campo para password
password_label = tk.Label(root, text='Digite a sua password:',bg=CORFUNDO, fg=CORTEXTO, font=("Arial", 14, 'bold'))
password_label.pack(pady=20)

password_entry = tk.Entry(root, width=30, show='*')
password_entry.pack()

#Botão
registar_button = tk.Button(root, text= 'Registar', width=10, command=registar)
registar_button.pack(pady= (25, 0))

# mensagem informativa
msg_label = tk.Label(root, text='',bg=CORFUNDO, fg=CORTEXTO, font=("Arial", 14, 'bold'))
msg_label.pack(pady=30)

# Por último: Iniciar o ciclo de eventos, ou seja, abrir a janela
root.mainloop()