# -*- encoding: utf-8 -*-


import xlwt

def grafico(linha, coluna, nline):

# Definindo planilha
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Jogos')
    ws.write(nline,1, linha)
    ws.write(nline,2, coluna)
    wb.save('teste.xls')
# Títulos das colunas
#titles = ['identificador','sequencia']

# Escrevendo títulos na primeira linha do arquivo
#for i in range(len(titles)):
 #   ws.write(0, i, titles[i])

# Definindo largura das células das sequência
#for i in range(1,50):
#    ws.col(i).width = 512

#i = 1

#for id_sequencia in sequencias.keys():

    # Obtendo a sequência do dicionário
    #sequencia = sequencias[id_sequencia]

    # Escrevendo o identificar na 1ª coluna da linha i
    #ws.write(i, 0, id_sequencia)

    #for j in range(len(sequencia)):
    #    if j < len(sequencia):
    #        if sequencia[j]=='A':
    #            ws.write(i, 1+j, sequencia[j])#, styleA)
    #        elif sequencia[j]=='C':
    #            ws.write(i, 1+j, sequencia[j])#, styleC)
    #        elif sequencia[j]=='G':
    #            ws.write(i, 1+j, sequencia[j])#, styleG)
    #        elif sequencia[j]=='T':
    #            ws.write(i, 1+j, sequencia[j])#, styleT)
    #        else:
    #            ws.write(i, 1+j, sequencia[j])
    #    else:
    #        ws.write(i, 1+j, '')
    #i += 1

# Salvando
#wb.save('sequencias.xls')