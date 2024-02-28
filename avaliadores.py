import openpyxl
import datetime

class Pendentes():
    def coletar_avaliacoes(username):
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")

        # Abre o arquivo Excel
        workbook = openpyxl.load_workbook(f'Q:\GROUPS\BR_SC_JGS_WM_LOGISTICA\PCP\Robert\Vários\Avaliação\Avaliação {year}\Colaboradores.xlsm')

        # Seleciona a planilha desejada
        sheet = workbook['AvaliadorxAvaliado']

        avaliacoes_pendentes = []

        # Percorre as células da coluna 1 e coluna 2
        for row in sheet.iter_rows(min_row=1, max_col=3, max_row=sheet.max_row):
            valor_coluna_1 = row[0].value
            valor_coluna_2 = row[1].value
            status_atual = row[2].value
            if valor_coluna_1 == username and (not status_atual):
                avaliacoes_pendentes.append(valor_coluna_2)

        # Fechar o arquivo após terminar de usar
        workbook.close()
        
        return avaliacoes_pendentes

