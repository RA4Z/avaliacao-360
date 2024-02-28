from avaliadores import Pendentes
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
            print(selecionados.selecionado)
            avalia = QuizApp(selecionados.selecionado, username,'Analista Júnior')
            avalia.start()
    except:
        pass
else:
    print('Não há avaliações pendentes para o usuário logado!')
