import pandas as pd
from openpyxl import Workbook

#pd.set_option('display.max_colwidth', None)

numero = 1
while numero <= 6:
    numero += 1

    print("Insira o diretório do arquivo: ")

    arquivo_csv = input()
    read_file = pd.read_csv(arquivo_csv, encoding="ISO-8859-1")

    arquivo_xlsx = arquivo_csv.replace("csv","xlsx")
    writer = pd.ExcelWriter(arquivo_xlsx, engine='openpyxl')
    # arquivo_csv = arquivo_csv.replace("csv","xlsx")
    read_file.to_excel(writer, sheet_name='Planilha1', na_rep='', float_format=None, columns=None, header=True, index=False, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, inf_rep='inf', freeze_panes=None, storage_options=None, engine_kwargs=None)
   
    sheet = writer.sheets['Planilha1']

    for column in sheet.columns:
        max_length = 0
        column = [str(cell.value) for cell in column]
        for cell in column:
            try:
                if len(cell) > max_length:
                    max_length=len(cell)
            except:
                pass
        adjusted_width = (max_length + 2)
        sheet.column_dimensions[column[0]].width = adjusted_width

    print("O arquivo foi convertido com sucesso!\n")
