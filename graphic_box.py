import tkinter as tk
from tkinter import messagebox
import keyboard
from export_result import Exportar
from perguntas import Questionario
from avaliadores import Pendentes
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class QuizApp:
    def __init__(self, user_avaliado, user_avaliador, avaliado_cargo):
        self.master = tk.Tk()
        self.master.title(f"Avaliação 360 - Avaliando {user_avaliado} de cargo {avaliado_cargo}")
        self.master.geometry("1384x800")
        self.master.resizable(False, False)
        self.aba = 1

        self.total = 0
        self.guias = ['|1.0|', '2.0', '3.0', '4.0', '5.0', '6.0', '7.0', '8.0', '9.0', '10.0']

        self.plot_grafico()
        self.user_avaliado = user_avaliado
        self.user_avaliador = user_avaliador
        self.avaliado_cargo = avaliado_cargo
        try:
            self.imagem = tk.PhotoImage(file=f"Q:\\GROUPS\\BR_SC_JGS_WM_LOGISTICA\\PCP\\Robert\\Vários\\Avaliação"
                                             f"\\Imagens\\Colaboradores\\{self.user_avaliado}.png")
        except:
            self.imagem = tk.PhotoImage(file=f"Q:\\GROUPS\\BR_SC_JGS_WM_LOGISTICA\\PCP\\Robert\\Vários\\Avaliação"
                                             f"\\Imagens\\Colaboradores\\USER.png")

        self.texto_status = tk.Label(self.master, text='Total: 0\n Média: 0.0', font=("Arial", 10))
        self.imagem_label = tk.Label(self.master, image=self.imagem)
        self.imagem_label.config(width=150, height=150)

        keyboard.on_press(self.on_key_press)

        self.questions = []
        for i in range(len(questionario)):
            if self.aba < float(questionario[i]['numero']) < self.aba + 1:
                self.questions.append(questionario[i])

        self.titulo = topicos_quest[self.aba - 1]['titulo']
        self.topico = topicos_quest[self.aba - 1]['topico']
        self.title_label = tk.Label(self.master, text=f"- - - - - - - - - - - - - - - {self.topico} - - - - - - - - - "
                                                      f"- - - - - -" +
                                                      f"\n\n{self.titulo}", font=("Arial", 18), wraplength=900)
        self.geral_frame = tk.Frame(self.master)
        self.obs_frame = tk.Frame(self.master)
        self.button_frame = tk.Frame(self.master)
        self.next_button = tk.Button(self.button_frame, text="Próximo", font=("Arial", 12), command=self.next_screen)

        self.guias_disponiveis = tk.Label(self.master, text=self.guias, font='Helvetica 12 bold', fg='#0078D7')
        self.guias_disponiveis.bind("<Button-1>", self.clique_na_lista)
        self.guias_disponiveis.bind("<Enter>", self.mudar_cursor)
        self.guias_disponiveis.bind("<Leave>", self.restaurar_cursor)

        self.texto_entry = tk.Text(self.obs_frame, wrap="word", height=5, width=100)
        self.creditos = tk.Label(self.master, text="Sistema de Avaliação 360 PCP WEN, desenvolvido por Robert Aron "
                                                   "Zimmermann - 2024", font='Helvetica 12 bold', fg='#0078D7',
                                 wraplength=1000)

        self.create_widgets()

    def mudar_cursor(self, event):
        self.guias_disponiveis.config(cursor="hand2")

    def restaurar_cursor(self, event):
        self.guias_disponiveis.config(cursor="")

    def clique_na_lista(self, event):
        texto_completo = self.guias_disponiveis.cget("text")
        x = event.x
        y = event.y
        indice = self.get_char_index(texto_completo, x, y)
        linha_clicada = texto_completo.count('.0', 0, indice) + 1
        item_clicado = int(str(texto_completo.split('.0')[linha_clicada - 1]).replace('|', '').strip())
        self.aba = item_clicado
        self.config()
        if self.aba == 10:
            self.atualizar_grafico()
            self.obs_frame.pack(pady=20)
            self.canvas.get_tk_widget().pack()
            self.next_button.config(text='Finalizar Avaliação', command=self.finalizar_avaliacao)

    def get_char_index(self, text, x, y):
        width = self.guias_disponiveis.winfo_width()
        height = self.guias_disponiveis.winfo_height()
        indice = int((x / width) * len(text))
        return min(indice, len(text) - 1)

    def start(self):
        self.master.mainloop()

    def plot_grafico(self):
        self.x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # Criar o gráfico de barras
        self.fig, self.ax = plt.subplots()
        self.bars = self.ax.bar(self.x, self.y)  # Usar a função bar() para criar as barras
        self.ax.set_xlabel('Módulos')
        self.ax.set_ylabel('Média')
        self.ax.set_title('Resumo Avaliação')

        # Adicionar o texto da dica de ferramenta
        self.texto_tooltip = self.ax.text(0, 0, '', alpha=0.0)
        self.fig.canvas.mpl_connect('motion_notify_event', self.hover)

        # Adicionar o gráfico à interface Tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

    def atualizar_grafico(self):
        # Atualizar os dados do gráfico
        for number in range(len(self.y)):
            soma_grafico = 0
            contagem = 0
            for i in range(len(questionario)):
                if number + 1 < float(questionario[i]['numero']) < number + 2:
                    soma_grafico += questionario[i]['score']
                    contagem += 1
            if contagem != 0:
                self.y[number] = soma_grafico / contagem
            else:
                self.y[number] = 0
                # Atualizar as alturas das barras
        for bar, height in zip(self.bars, self.y):
            bar.set_height(height)

        # Atualizar o gráfico
        self.canvas.draw()

    def hover(self, event):
        if event.inaxes == self.ax:
            for index, bar in enumerate(self.bars):
                if bar.contains(event)[0]:
                    x = bar.get_x() + bar.get_width() / 2
                    y = bar.get_height()
                    self.texto_tooltip.set_text(f'Média: {y:.2f}, Aba: {index + 1}')
                    self.texto_tooltip.set_position((x, y))
                    self.texto_tooltip.set_alpha(1.0)
                    self.canvas.draw_idle()
                    return
        self.texto_tooltip.set_alpha(0.0)
        self.canvas.draw_idle()

    def create_widgets(self):
        self.imagem_label.place(x=0, y=0)
        self.texto_status.place(x=0, y=150)
        self.guias_disponiveis.place(x=1050, y=0)

        self.title_label.pack(pady=10)

        self.option_vars = []
        self.geral_frame.pack()

        self.config()

        obs_label = tk.Label(self.obs_frame, text='Escreva sua Observação', font=("Arial", 14))
        obs_label.pack()  # Aumento do espaço entre as perguntas
        self.texto_entry.pack(padx=10, pady=0)

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
            self.atualizar_grafico()
            self.obs_frame.pack(pady=20)
            self.canvas.get_tk_widget().pack()
            self.next_button.config(text='Finalizar Avaliação', command=self.finalizar_avaliacao)

    def prev_screen(self):
        if self.aba > 1:
            self.aba = self.aba - 1
            self.config()

    def finalizar_avaliacao(self):
        for question in questionario:
            if question['score'] == 0:
                messagebox.showwarning(title='Erro na avaliação',
                                       message=f"A questão {question['numero']} não foi respondida!")
                return
        if self.texto_entry.get("1.0", tk.END).replace("\n", "").strip() == '':
            messagebox.showwarning(title='Erro na avaliação',
                                   message=f"O campo observação não pode estar em branco!")
            return

        result = messagebox.askquestion(title='Finalizar avaliação',
                                        message='Tem certeza de que deseja enviar a avaliação?')
        if result == 'yes':
            try:
                export = Exportar(self.user_avaliador, self.user_avaliado, self.avaliado_cargo,
                                  self.texto_entry.get("1.0", tk.END).replace("\n", ""), questionario)
                export.export_data()
                Pendentes.concluir_avaliacao(self.user_avaliador, self.user_avaliado)
                messagebox.showinfo(title='Avaliação Enviada', message="Avaliação enviada com sucesso!")
                self.master.destroy()
            except:
                messagebox.showerror(title='Erro inesperado',
                                     message="Algum erro inesperado ocorreu! Tente novamente mais tarde!")
        else:
            return

    def keypress(event):
        print('Algo')
        if event.keysym == 'RightArrow':
            print('Direita')
        if event.keysym == 'LeftArrow':
            print('Esquerda')

    def config(self):
        self.obs_frame.pack_forget()
        self.canvas.get_tk_widget().pack_forget()
        self.titulo = topicos_quest[self.aba - 1]['titulo']
        self.topico = topicos_quest[self.aba - 1]['topico']
        self.next_button.config(text='Próximo', command=self.next_screen)
        self.title_label.config(
            text=f"- - - - - - - - - - - - - - - {self.topico} - - - - - - - - - - - - - - -\n\n{self.titulo}")
        self.questions = []

        for i in range(len(self.guias)):
            if i == self.aba - 1:
                self.guias[i] = f'|{self.aba}.0|'
            else:
                self.guias[i] = self.guias[i].replace('|', '')

        for i in range(len(questionario)):
            if float(questionario[i]['numero']) > self.aba and float(questionario[i]['numero']) < self.aba + 1:
                self.questions.append(questionario[i])
        self.guias_disponiveis.config(text=self.guias)
        for widget in self.geral_frame.winfo_children():
            widget.destroy()
        self.construir_perguntas()

    def construir_perguntas(self):
        for index, question in enumerate(self.questions):
            question_label = tk.Label(self.geral_frame, text=question['pergunta'], font=("Arial", 14), wraplength=1000)
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
                option_button = tk.Radiobutton(options_frame, text=option, value=option, font=("Arial", 10),
                                               variable=var, wraplength=250,
                                               command=lambda index=index, i=i: self.on_option_selected(index, i))
                option_button.pack(side="left", padx=10)

    def on_option_selected(self, question_index, option_index):
        indice = next((index for index, pergunta in enumerate(questionario) if
                       pergunta['numero'] == f"{self.aba}.{question_index + 1}"), None)
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
        self.total = 0
        for question in questionario:
            self.total = self.total + question['score']
        self.texto_status.config(text=f'Total: {self.total}\n Média: {round(self.total / len(questionario), 2)}')
        self.atualizar_grafico()

    def on_key_press(self, event):
        if event.name == 'right':
            self.next_screen()
        if event.name == 'left':
            self.prev_screen()


questionario = Questionario.coletar_perguntas()
topicos_quest = Questionario.coletar_cabecalhos()
