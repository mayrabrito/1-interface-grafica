import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Perquisa 15 Widgets do TKinter")
root.geometry("1000x800")

#1- FRAME: Funciona como um "container" para organizar e agrupar outros widgets.
## tk.Frame(variável,).pack
agrupar = tk.LabelFrame(root, text="1. Frame", padx=10, pady=10)
agrupar.pack(fill="x", padx=10, pady=5)
tk.Frame(agrupar, width=100, height=30, bg="blue").pack()

# 2- CHECKBUTTON: Uma caixa de seleção que permite ao usuário escolher entre dois estados (ligado/desligado).
## tk.Checkbutton(variável, text="Opção").pack
caixa_escolha = tk.LabelFrame(root, text="2. Checkbutton")
caixa_escolha.pack(fill="x", padx=10, pady=5)
tk.Checkbutton(caixa_escolha, text="Opção Marcada").pack()

# 3- RADIOBUTTON: Permite escolher apenas uma opção entre várias de um grupo.
## tk.Radiobutton(variável, text="Escolha", value=1).pack
escolha_unica = tk.LabelFrame(root, text="3. Radiobutton")
escolha_unica.pack(fill="x", padx=10, pady=5)
tk.Radiobutton(escolha_unica, text="Opção A", value=1).pack(side="left")
tk.Radiobutton(escolha_unica, text="Opção B", value=2).pack(side="left")

# 4 e 5 - LISTBOX + SCROLLBAR
# LISTBOX: Exibe uma lista de itens onde o usuário pode selecionar um ou mais.
## tk.Listbox(variável)
# SCROLLBAR: Adiciona barras de rolagem para navegar em conteúdos que não cabem na janela (como no Listbox ou Text).
## tk.Scrollbar(variável)
listagem_controle = tk.LabelFrame(root, text="4 e 5. Listbox e Scrollbar")
listagem_controle.pack(fill="x", padx=10, pady=5)
scroll = tk.Scrollbar(listagem_controle)
scroll.pack(side="right", fill="y")
lista = tk.Listbox(listagem_controle, yscrollcommand=scroll.set, height=3)
for i in range(10): lista.insert("end", f"Item {i}")
lista.pack(side="left", fill="both", expand=True)
scroll.config(command=lista.yview)

# 6- SCALE: Um controle deslizante (slider) para selecionar um valor numérico em um intervalo.
## tk.Scale(variável, from_=0, to=100, orient="horizontal").pack
slider = tk.LabelFrame(root, text="6. Scale (Deslizante)")
slider.pack(fill="x", padx=10, pady=5)
tk.Scale(slider, from_=0, to=100, orient="horizontal").pack(fill="x")

# 7- SPINBOX: Uma variação da entrada de texto que permite selecionar números através de setas "para cima" e "para baixo".
## tk.Spinbox(parent, from_=0, to=10)
setas = tk.LabelFrame(root, text="7. Spinbox")
setas.pack(fill="x", padx=10, pady=5)
tk.Spinbox(setas, from_=0, to=10).pack()

# 8- MENU (Aparecerá no topo da janela): Cria barras de menu no topo da janela (como o "File" e "Edit" do próprio GitHub Desktop).
## tk.Menu(variável)
menu_barra = tk.Menu(root)
menu_arquivo = tk.Menu(menu_barra, tearoff=0)
menu_arquivo.add_command(label="Exemplo")
menu_barra.add_cascade(label="8. Menu", menu=menu_arquivo)
root.config(menu=menu_barra)

# 9- MESSAGE: Similar ao Label, mas formata automaticamente textos longos em várias linhas.
## tk.Message(variável, text="Texto longo...")
texto_longo = tk.LabelFrame(root, text="9. Message")
texto_longo.pack(fill="x", padx=10, pady=5)
tk.Message(texto_longo, text="Este é um texto longo que quebra sozinho.", width=200).pack()

# 10- CANVAS: Uma área para desenhar formas geométricas, gráficos ou exibir imagens personalizadas.
## tk.Canvas(variável, width=100, height=100)
imagens = tk.LabelFrame(root, text="10. Canvas (Desenho)")
imagens.pack(fill="x", padx=10, pady=5)
canv = tk.Canvas(imagens, width=200, height=50, bg="white")
canv.pack()
canv.create_line(0, 0, 200, 50, fill="red")

# 11- TOPLEVEL (Abre uma nova janela ao clicar): Cria uma janela separada da principal (uma janela pop-up ou de diálogo).
## tk.Toplevel(variável)
def abrir_popup():
    tk.Toplevel(root).title("Janela 11")
tk.Button(root, text="Abrir 11. Toplevel", command=abrir_popup).pack(pady=10)

# 12- COMBOBOX: Uma lista suspensa (dropdown) que permite escolher uma opção de uma lista pré-definida.
## ttk.Combobox(variável, values=["Opção 1", "Opção 2"])
from tkinter import ttk # Necessário para o Combobox
lista_suspensa = tk.LabelFrame(root, text="12. Combobox")
lista_suspensa.pack(fill="x", padx=10, pady=5)
combo = ttk.Combobox(lista_suspensa, values=["Python", "Java", "C++", "JavaScript"])
combo.set("Selecione uma linguagem")
combo.pack(pady=5)

# 13- LABELFRAME: Um container com uma borda e um título (exatamente o que você está usando para organizar este projeto!).
## tk.LabelFrame(variável, text="Título")
exemplo_moldura = tk.LabelFrame(root, text="13. LabelFrame (Eu sou um!)", labelanchor="n")
exemplo_moldura.pack(fill="x", padx=10, pady=5)
tk.Label(exemplo_moldura, text="Eu organizo outros widgets com um título.").pack()

# 14- PROGRESSBAR: Uma barra que mostra o progresso de uma tarefa ou carregamento.
## ttk.Progressbar(variável, length=100, mode='determinate')
barra_progresso = tk.LabelFrame(root, text="14. Progressbar")
barra_progresso.pack(fill="x", padx=10, pady=5)
progresso = ttk.Progressbar(barra_progresso, length=200, mode='determinate')
progresso.pack(pady=5)
progresso['value'] = 70 # Define a barra em 70%

# 15- SEPARATOR: Uma linha horizontal ou vertical simples para separar visualmente as seções.
## ttk.Separator(variável, orient="horizontal")
divisor_visual = tk.LabelFrame(root, text="15. Separator")
divisor_visual.pack(fill="x", padx=10, pady=5)
tk.Label(divisor_visual, text="Texto Acima").pack()
ttk.Separator(divisor_visual, orient="horizontal").pack(fill="x", pady=5)
tk.Label(divisor_visual, text="Texto Abaixo").pack()


root.mainloop()

