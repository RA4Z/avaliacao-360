import tkinter as tk
import keyboard
from perguntas import Questionario

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Avaliação 360")
        self.master.geometry("1384x800")      
        self.master.resizable(False, False)  
        self.aba = 1

        keyboard.on_press(self.on_key_press)
        #self.imagem = tk.PhotoImage(file="Q:\GROUPS\BR_SC_JGS_WM_LOGISTICA\PCP\Robert\BannerAvalia.png")
        #self.imagem_label = tk.Label(self.master, image=self.imagem)
        #self.imagem_label.place(x = 0, y = 0)

        self.questions = []
        for i in range(len(questionario)):
            if float(questionario[i]['numero']) > self.aba and float(questionario[i]['numero']) < self.aba + 1:
                self.questions.append(questionario[i])

        self.titulo = topicos_quest[self.aba-1]['titulo']
        self.topico = topicos_quest[self.aba-1]['topico']
        self.title_label = tk.Label(self.master, text=f"- - - - - - - - - - - - - - - {self.topico} - - - - - - - - - - - - - - -" +
                               f"\n\n{self.titulo}", font=("Arial", 18), wraplength=1000)
        self.geral_frame = tk.Frame(self.master)
        self.obs_frame = tk.Frame(self.master)
        self.button_frame = tk.Frame(self.master)
        self.next_button = tk.Button(self.button_frame, text="Próximo", font=("Arial", 12), command=self.next_screen)

        self.creditos = tk.Label(self.master, text="Sistema de Avaliação 360 PCP WEN, desenvolvido por Robert Aron Zimmermann - 2024", font='Helvetica 12 bold',fg='#0078D7', wraplength=1000)

        self.create_widgets()

    def create_widgets(self):
                
        self.title_label.pack(pady=10)

        # Lista para armazenar as variáveis de controle dos botões de opção de cada pergunta
        self.option_vars = []
        self.geral_frame.pack()

        self.config()

        obs_label = tk.Label(self.obs_frame,text='Escreva sua Observação', font=("Arial", 14))
        obs_label.pack()  # Aumento do espaço entre as perguntas
        texto_entry = tk.Text(self.obs_frame, wrap="word", height=10, width=100)
        texto_entry.pack(padx=10, pady=0)

        # Créditos
        self.creditos.pack(pady=5, side="bottom")

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
            self.obs_frame.pack(pady=20)
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

    def keypress(event): 
        print('Algo')
        if event.keysym == 'RightArrow': 
            print('Direita')
        if event.keysym == 'LeftArrow': 
            print('Esquerda')
            
    def config(self):
        self.obs_frame.pack_forget()
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

    def on_key_press(self,event):
        if event.name == 'right':
            self.next_screen()
        if event.name == 'left':
            self.prev_screen()

questionario = Questionario.coletar_perguntas()
topicos_quest = Questionario.coletar_cabecalhos()
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
