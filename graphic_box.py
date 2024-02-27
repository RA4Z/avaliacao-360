import tkinter as tk
from perguntas import Questionario

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Avaliação 360")
        self.master.geometry("1200x800")
        self.aba = 1

        self.questions = []
        for i in range(len(questionario)):
            if float(questionario[i]['numero']) > self.aba and float(questionario[i]['numero']) < self.aba + 1:
                self.questions.append(questionario[i])

        self.titulo = topicos_quest[self.aba-1]['titulo']
        self.topico = topicos_quest[self.aba-1]['topico']
        self.title_label = tk.Label(self.master, text=f"- - - - - - - - - - - - - - - {self.topico} - - - - - - - - - - - - - - -" +
                               f"\n\n{self.titulo}", font=("Arial", 18), wraplength=1000)
        self.geral_frame = tk.Frame(self.master)
        self.button_frame = tk.Frame(self.master)
        self.next_button = tk.Button(self.button_frame, text="Próximo", font=("Arial", 12), command=self.next_screen)
        self.create_widgets()

    def create_widgets(self):
                
        self.title_label.pack(pady=20)

        # Lista para armazenar as variáveis de controle dos botões de opção de cada pergunta
        self.option_vars = []
        self.geral_frame.pack()
        self.config()

        # Botões
        self.button_frame.pack(pady=20, side="bottom")  # Coloque o frame dos botões na parte inferior

        prev_button = tk.Button(self.button_frame, text="Anterior", font=("Arial", 12), command=self.prev_screen)
        prev_button.pack(side="left", padx=10)

        self.next_button.pack(side="left", padx=10)

    def next_screen(self):
        if self.aba < 10:
            self.aba = self.aba + 1
            self.config()

        if self.aba == 10:
            self.next_button.config(text='Finalizar Avaliação',command=self.finalizar_avaliacao)

    def prev_screen(self):
        if self.aba > 1:
            self.aba = self.aba - 1
            self.config()

    def finalizar_avaliacao(self):
        for question in questionario:
            if question['score'] == 0:
                print(f"A questão {question['numero']} não foi respondida!")
                return
        print('Avaliação finalizada!')

    def config(self):
        self.titulo = topicos_quest[self.aba-1]['titulo']
        self.topico = topicos_quest[self.aba-1]['topico']
        self.next_button.config(text='Próximo', command=self.next_screen)
        self.title_label.config(text=f"- - - - - - - - - - - - - - - {self.topico} - - - - - - - - - - - - - - -\n\n{self.titulo}")
        self.questions = []
        for i in range(len(questionario)):
            if float(questionario[i]['numero']) > self.aba and float(questionario[i]['numero']) < self.aba + 1:
                self.questions.append(questionario[i])
        for widget in self.geral_frame.winfo_children():
            widget.destroy()
        self.construir_perguntas()

    def construir_perguntas(self):
        for index, question in enumerate(self.questions):
            question_label = tk.Label(self.geral_frame,text=question['pergunta'], font=("Arial", 14), wraplength=1000)
            question_label.pack(pady=10)  # Aumento do espaço entre as perguntas
            options_frame = tk.Frame(self.geral_frame)
            options_frame.pack()

            # Variável de controle para cada grupo de opções
            var = tk.StringVar(value=question['selecionado'])
            self.option_vars.append(var)

            options = [
                question['pontos10'],
                question['pontos8'],
                question['pontos6'],
                question['pontos4'],
            ]

            for i, option in enumerate(options):
                option_button = tk.Radiobutton(options_frame, text=option, value=option, font=("Arial", 10), variable=var, wraplength=250,
                                            command=lambda index=index, i=i: self.on_option_selected(index, i))
                option_button.pack(side="left", padx=10)

    def on_option_selected(self, question_index, option_index):
        indice = next((index for index, pergunta in enumerate(questionario) if pergunta['numero'] == f"{self.aba}.{question_index + 1}"), None)
        if option_index == 0: 
            questionario[indice]['score'] = 10 
            questionario[indice]['selecionado'] = questionario[indice]['pontos10']
        if option_index == 1: 
            questionario[indice]['score'] = 8
            questionario[indice]['selecionado'] = questionario[indice]['pontos8']
        if option_index == 2: 
            questionario[indice]['score'] = 6
            questionario[indice]['selecionado'] = questionario[indice]['pontos6']
        if option_index == 3: 
            questionario[indice]['score'] = 4
            questionario[indice]['selecionado'] = questionario[indice]['pontos4']

questionario = Questionario.coletar_perguntas()
topicos_quest = Questionario.coletar_cabecalhos()
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
