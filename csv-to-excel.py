import pandas as pd

pd.set_option('display.max_colwidth', None)

numero = 1
while numero <= 6:
    numero += 1

    print("Insira o diretório do arquivo: ")

    arquivo_csv = input()
    read_file = pd.read_csv(arquivo_csv, encoding="ISO-8859-1")

    arquivo_csv = arquivo_csv.replace("csv","xlsx")
    read_file.to_excel(arquivo_csv, sheet_name='planilha', na_rep='NaN', float_format=None, columns=None, header=True, index=False, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, inf_rep='inf', freeze_panes=None, storage_options=None, engine_kwargs=None)
   
    print("O arquivo foi convertido com sucesso!\n")
