import datetime


class Exportar:
    def __init__(self, avaliador, avaliado, cargo, obs, questionario):
        self.total = 0
        self.contagem = 0

        self.avaliador = avaliador
        self.avaliado = avaliado
        self.cargo = cargo
        self.obs = str(obs).replace(';', ',')

        self.cabecalho = ('Colaborador avaliado;Cargo do colaborador avaliado;Colaborador avaliador;Total Geral;Média '
                          'Total;Observações;Data/Hora')
        self.dados = f'{self.avaliado};{self.cargo};{self.avaliador};total;media;{self.obs};{currentDateTime}'

        for question in questionario:
            self.total = self.total + question['score']
            self.contagem = self.contagem + 1
            self.cabecalho = self.cabecalho + f";{str(question['numero'])}"
            self.dados = self.dados + f";{str(question['score'])}"
        self.media = self.total / self.contagem

        self.dados = self.dados.replace('media', str(self.media))
        self.dados = self.dados.replace('total', str(self.total))

    def export_data(self):
        with open(caminho + self.avaliador + '_avaliando_' + self.avaliado + '.txt', 'w') as f:
            f.write(self.cabecalho + '\n')
            f.write(self.dados + '\n')


currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")

caminho = f'Q:/GROUPS/BR_SC_JGS_WM_LOGISTICA/PCP/Robert/Vários/Avaliação/Avaliação {year}/Resultados/Gabarito_'
