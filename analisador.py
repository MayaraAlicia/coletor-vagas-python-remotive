import pandas as pd
import sqlite3


con = sqlite3.connect('vagas.db')

df = pd.read_sql_query("SELECT * FROM VAGAS", con)
print (f"Total de vagas no banco de dados: {len(df)}")
print('--- Listagem de todas as vagas ---')
print (df)

#"Quantas dessas vagas são para Nível Sênior e quantas são para Júnior?"

senior = df['TITULO'].str.contains('Sênior|Senior|Sr|Sr.|Lead|Principal|Staff|Head', case = False, regex=True )
junior = df['TITULO'].str.contains('Junior|Júnior|Jr.|Jr|Entry Level|Intern|Trainee', case = False, regex=True )
outros = len(df) - senior.sum() - junior.sum()

print (f"Vagas para Nível Sênior: {senior.sum()}")
print (f"Vagas para Nível Júnior: {junior.sum()}")
print (f"Vagas para Outros Níveis: {outros}")