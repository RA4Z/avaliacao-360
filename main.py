from avaliadores import Pendentes
from perguntas import Questionario

pendencias = Pendentes.coletar_avaliacoes()
questionario = Questionario.coletar_perguntas()
topicos_quest = Questionario.coletar_cabecalhos()
aba_atual = 8
if len(pendencias) > 0:
    print(f'Escolha algum usuário para avaliar: {pendencias}')  #FAZER ESQUEMA PRA ESCOLHER USUÁRIO
    for topico in topicos_quest:
        if float(topico['numero']) == float(aba_atual):
            print(f"{topico['titulo']} - {topico['topico']}")

    for i in range(len(questionario)):  #MOSTRAR TELA DE ACORDO COM A ABA ESCOLHIDA NO MOMENTO
        if float(questionario[i]['numero']) > aba_atual and float(questionario[i]['numero']) < aba_atual + 1:
            print(f"{questionario[i]['numero']} - {questionario[i]['pergunta']}")
else:
    print('Não há avaliações pendentes para o usuário logado!')