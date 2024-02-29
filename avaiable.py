import tkinter as tk

class Select():
    def __init__(self, pendencias):
        self.pendencias = pendencias
        self.root = tk.Tk()
        self.root.geometry("350x450")      
        self.root.resizable(False, False)  
        self.root.title("Selecionar Colaborador")

        self.imagem = tk.PhotoImage(file="Q:\\GROUPS\\BR_SC_JGS_WM_LOGISTICA\\PCP\\Robert\\Vários\\Avaliação\\Imagens\\Colaboradores\\USER.png")
        self.imagem_label = tk.Label(self.root, image=self.imagem)
        self.imagem_label.config(width=150, height=150)
        self.title_label = tk.Label(self.root, text="Selecione um colaborador para Avaliar...", font=("Arial", 15), wraplength=300)
        self.lista_nomes = tk.Listbox(self.root)
        self.lista_nomes.bind("<<ListboxSelect>>", self.trocar_imagem)

        self.botao_selecionar = tk.Button(self.root, text="Selecionar", command=self.selecionar_nome)
        for nome in pendencias:
            self.lista_nomes.insert(tk.END, nome['colaborador'])
        self.estilizar_tela()

        self.selecionado = None

    def trocar_imagem(self, event):
        try:
            nome_selecionado = self.lista_nomes.get(tk.ACTIVE)
            self.imagem = tk.PhotoImage(file=f"Q:\\GROUPS\\BR_SC_JGS_WM_LOGISTICA\\PCP\\Robert\\Vários\\Avaliação\\Imagens\\Colaboradores\\{nome_selecionado}.png")
        except:
            self.imagem = tk.PhotoImage(file="Q:\\GROUPS\\BR_SC_JGS_WM_LOGISTICA\\PCP\\Robert\\Vários\\Avaliação\\Imagens\\Colaboradores\\USER.png")
        self.imagem_label.config(image=self.imagem)

    def estilizar_tela(self):
        self.title_label.pack()
        self.lista_nomes.pack(padx=10, pady=10)
        self.botao_selecionar.pack(pady=5)
        self.imagem_label.pack()

    def selecionar_nome(self):
        self.selecionado = self.lista_nomes.get(tk.ACTIVE)
        self.root.destroy()
        
    def exibir(self):
        self.root.mainloop()
        return self.selecionado