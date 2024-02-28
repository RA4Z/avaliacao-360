from avaliadores import Pendentes
from tkinter import messagebox
import getpass
from graphic_box import QuizApp
from avaiable import Select

username = getpass.getuser().upper()
pendencias = Pendentes.coletar_avaliacoes(username)
if len(pendencias) > 0:
    try:
        selecionados = Select(pendencias)
        selecionados.exibir()
        if selecionados.selecionado != None:
            indice = next((index for index, colab in enumerate(pendencias) if colab['colaborador'] == selecionados.selecionado), None)
            avalia = QuizApp(selecionados.selecionado, username,pendencias[indice]['cargo'])
            avalia.start()
    except:
        pass
else:
    messagebox.showinfo(title='Sem Avaliações Pendentes', message="Não há avaliações pendentes para o usuário logado!")
