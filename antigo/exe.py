# -*- encoding: utf-8 -*-
# seq2xls.py - script para transformar sequências de nucleotídeos
#              (DNA) em arquivos de Excel (xls) com cores

# Criado em: 15/05/2012
# Última modificação: 03/07/2012
# Leandro Lima 

# Essa é a biblioteca a ser importada
import xlwt

# Aqui você define um estilo a ser usado

# (em quantas células você desejar).

# Iremos definir as seguintes cores (para o fundo da célula):
# A -> vermelho
styleA = xlwt.easyxf('pattern: pattern solid, fore_colour red;')

# C -> verde
styleC = xlwt.easyxf('pattern: pattern solid, fore_colour green;')

# G -> amarelo
styleG = xlwt.easyxf('pattern: pattern solid, fore_colour yellow;')

# T -> azul
styleT = xlwt.easyxf('pattern: pattern solid, fore_colour blue;')


# Definindo as sequências
sequencias = {'sequencia 1':'ACTGATCATGACATAGTAACCATGACATAGAA',
              'sequencia 2':'CTAGCATGCATGACTAGCATGACTGACTGACT',
              'sequencia 3':'CATCGACTCGACTCGACATCAGCAGCAGCATG',
              'sequencia 4':'CTGACTAGCAGATCAGCATACGACTAGCCACA',
              'sequencia 5':'CTAGCAGGACGACAGATTGACAGCAGAGCACA',
              'sequencia 6':'AATCACATCACGGCATACGACGACTAGCAGTA',
}

# Definindo planilha
wb = xlwt.Workbook()
ws = wb.add_sheet('Sequencias')

# Títulos das colunas
titles = ['identificador','sequencia']

# Escrevendo títulos na primeira linha do arquivo
for i in range(len(titles)):
    ws.write(0, i, titles[i])

# Definindo largura das células das sequência
for i in range(1,50):
    ws.col(i).width = 512

i = 1

for id_sequencia in sequencias.keys():

    # Obtendo a sequência do dicionário
    sequencia = sequencias[id_sequencia]

    # Escrevendo o identificar na 1ª coluna da linha i
    ws.write(i, 0, id_sequencia)

    for j in range(len(sequencia)):
        if j < len(sequencia):
            if sequencia[j]=='A':
                ws.write(i, 1+j, sequencia[j])#, styleA)
            elif sequencia[j]=='C':
                ws.write(i, 1+j, sequencia[j])#, styleC)
            elif sequencia[j]=='G':
                ws.write(i, 1+j, sequencia[j])#, styleG)
            elif sequencia[j]=='T':
                ws.write(i, 1+j, sequencia[j])#, styleT)
            else:
                ws.write(i, 1+j, sequencia[j])
        else:
            ws.write(i, 1+j, '')
    i += 1

# Salvando
wb.save('sequencias.xls')