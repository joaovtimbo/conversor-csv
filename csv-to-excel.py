import pandas as pd

print("Insira o diretório do arquivo: ")

arquivo_csv = input()
read_file = pd.read_csv(arquivo_csv)
arquivo_csv = arquivo_csv.replace("csv","xlsx")
read_file.to_excel(arquivo_csv, index=None, header=True)

print("O arquivo foi convertido com sucesso!")
