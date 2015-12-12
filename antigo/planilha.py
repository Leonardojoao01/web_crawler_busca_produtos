# -*- encoding: utf-8 -*-
import xlrd

book = xlrd.open_workbook("sequencias.xls")

 
    # print number of sheets
#print book.nsheets

    # print sheet names
#print book.sheet_names()
 
    # get the first worksheet
first_sheet = book.sheet_by_index(0)
 
    # read a row
#print first_sheet.row_values(0)
 
    # read a cell
cell = first_sheet.cell(2,1)
#print cell
print cell.value