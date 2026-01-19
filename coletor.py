import requests
import json
import sqlite3

url_site = "https://remotive.com/api/remote-jobs?category=software-dev&search=python"

response = requests.get(url_site)

if response.status_code == 200:
    con = sqlite3.connect('vagas.db')
    cur = con.cursor()

    dados = response.json()

    palavras_perigosas = ['DROP TABLE', 'DELETE FROM', 'INSERT', 'UPDATE VAGAS']
    vagas_perigosas = []


    vagas = dados['jobs']
    print (f"{len(vagas)} vagas encontradas")

    print (f"Primeira vaga: {vagas[0]['title']}")

    for vaga in vagas:
        titulo = vaga['title']
        empresa = vaga['company_name']
        cidade = vaga.get('candidate_required_location', 'Local não informado')
        url = vaga['url']
        data_coleta = vaga['publication_date']
        cur.execute('''INSERT OR IGNORE INTO VAGAS (TITULO, EMPRESA, CIDADE, DATA_COLETA, URL)
                    VALUES (?, ?, ?, ?, ?)''', (titulo, empresa, cidade, data_coleta, url))
        
        if any(palavra in titulo.upper() for palavra in palavras_perigosas):
            vagas_perigosas.append(titulo)
        
    print ("Vagas inseridas no banco de dados com sucesso.")
    
    if len(vagas_perigosas) != 0:
        print("⚠️ ALERTA: Possível tentativa de ataque detectada no título:")
        for vaga_suspeita in vagas_perigosas:
            print(f"- {vaga_suspeita}")
    con.commit()
    con.close() 



elif response.status_code == 404:
    print("Página não encontrada")

elif response.status_code == 500:
    print("Erro no servidor")

elif response.status_code == 403:
    print("Acesso proibido")

else:
    print("Ocorreu um erro desconhecido")