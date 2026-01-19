💼 Central de Vagas de Emprego para TI
Este projeto é um sistema de ETL (Extract, Transform, Load) desenvolvido em Python para automatizar a coleta, o armazenamento e a visualização de vagas de emprego voltadas para a área de tecnologia. O foco principal é extrair dados da API Remotive, processar os níveis de experiência (Júnior, Sênior, etc.) e exibir as informações de forma intuitiva em um dashboard.

🚀 Funcionalidades

- Extração Automática: Consome dados em tempo real da API Remotive filtrando por categorias de desenvolvimento de software.
- Banco de Dados Relacional: Armazena as vagas em um banco de dados SQLite local, garantindo persistência e evitando duplicidade por meio de URLs únicas.
- Análise de Dados: Utiliza a biblioteca Pandas para classificar as vagas por níveis de senioridade com base em palavras-chave no título.
- Dashboard Interativo: Interface web desenvolvida com Streamlit para visualização de gráficos e métricas do mercado.

🛠️ Tecnologias Utilizadas

- Linguagem: Python.
- Bibliotecas de Dados: Pandas (Análise) e Requests (Integração com API).
- Banco de Dados: SQLite3.
- Interface Gráfica: Streamlit.

📂 Estrutura do Projeto
O sistema é dividido em módulos para facilitar a manutenção e escalabilidade:

- bd.py: Script responsável por criar a tabela VAGAS no banco de dados SQLite.
- coletor.py: Realiza a requisição à API, filtra os dados e os insere no banco de dados utilizando segurança contra duplicidade.
- analisador.py: Processa o banco de dados e gera relatórios estatísticos sobre a quantidade de vagas por nível.
- dashboard.py: Constrói a interface visual com gráficos de barras e contadores de vagas.

🔧 Como Executar
1. Clone este repositório.
2. Instale as dependência.
3. Inicie o banco de dados.
4. Colete as vagas.
5. Execute o dashboard.
