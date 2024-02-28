from avaliadores import Pendentes
from graphic_box import QuizApp
from avaiable import Select

pendencias = Pendentes.coletar_avaliacoes()
if len(pendencias) > 0:
    try:
        selecionados = Select(pendencias)
        selecionados.exibir()
        if selecionados.selecionado != '':
            avalia = QuizApp(selecionados.selecionado,'ROBERTN','Analista Júnior')
            avalia.start()
    except:
        pass
else:
    print('Não há avaliações pendentes para o usuário logado!')
