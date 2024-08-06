# Sistema de Avaliação 360°

## Descrição

Este sistema implementa uma aplicação de avaliação 360 graus para colaboradores, utilizando interface gráfica e integração com planilhas Excel. Ele permite que os avaliadores respondam a perguntas sobre seus colegas, gerando relatórios com gráficos para visualização dos resultados.

## Funcionalidades

- Coleta de avaliações pendentes de um arquivo Excel.
- Interface gráfica amigável para responder às perguntas da avaliação.
- Geração de gráficos de barras para visualização das pontuações médias por módulo.
- Exportação dos resultados da avaliação para um arquivo de texto.
- Atualização do status da avaliação na planilha Excel.

## Arquivos

- **avaiable.py:** Interface gráfica para seleção do colaborador a ser avaliado.
- **avaliadores.py:** Métodos para gerenciar avaliações pendentes.
- **export_result.py:** Exporta os resultados da avaliação para um arquivo de texto.
- **graphic_box.py:** Interface gráfica principal da avaliação com perguntas, opções de resposta e gráfico de resultados.
- **main.py:** Ponto de entrada da aplicação, responsável por iniciar a interface gráfica e gerenciar o fluxo da avaliação.
- **perguntas.py:** Carrega as perguntas e títulos da avaliação a partir de um arquivo Excel.

## Dependências

- Python 3.x
- Tkinter
- Matplotlib
- xlrd (para ler arquivos .xls)
- openpyxl (para ler arquivos .xlsx)

## Melhorias Futuras

- Implementar tratamento de erros mais robusto.
- Adicionar documentação detalhada ao código.
- Melhorar o design da interface gráfica.
- Criar testes unitários para garantir a qualidade do código.
- Revisar e aprimorar a segurança da aplicação, especialmente no acesso a dados confidenciais.
- Otimizar o código para melhorar o desempenho, principalmente na leitura e escrita de dados em arquivos Excel.