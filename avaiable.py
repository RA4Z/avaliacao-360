import tkinter as tk

class Select():
    def __init__(self, pendencias):
        self.pendencias = pendencias
        self.root = tk.Tk()
        self.root.geometry("300x300")      
        self.root.resizable(False, False)  
        self.root.title("Selecionar Colaborador")

        self.lista_nomes = tk.Listbox(self.root)
        self.botao_selecionar = tk.Button(self.root, text="Selecionar", command=self.selecionar_nome)
        for nome in pendencias:
            self.lista_nomes.insert(tk.END, nome['colaborador'])
        self.estilizar_tela()

        self.selecionado = None

    def estilizar_tela(self):
        self.lista_nomes.pack(padx=10, pady=10)
        self.botao_selecionar.pack(pady=5)

    def selecionar_nome(self):
        self.selecionado = self.lista_nomes.get(tk.ACTIVE)
        self.root.destroy()
        
    def exibir(self):
        self.root.mainloop()
        return self.selecionado
