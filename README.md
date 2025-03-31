# 🌌 NASA API Proxy - Projeto Demonstrativo

## Sobre o Projeto
API desenvolvida em Python/Flask que consome dados públicos da NASA, criada para demonstrar habilidades.

## Tecnologias Utilizadas

Sistema Operacional: Ubuntu 24.04 LTS

Linguagem: Python 3.10+

Framework: Flask

Virtualização: Ambiente virtual Python (venv)

Testes de API: Bruno (alternativa ao Postman)

Gerenciamento de Variáveis: python-dotenv

## Como Usar

Pré-requisitos

- Python 3.10+

- Chave da API NASA (obtenha em api.nasa.gov)

- Pip (gerenciador de pacotes Python)

## Instalação 

```
git clone https://github.com/guinicolaci/nasa-api.git
cd nasa-api
```

```
pip install -r requirements.txt
```

```
- Edite o `.env` com sua chave da NASA:

  NASA_API_KEY=sua_chave_aqui
```

# Executanto o Projeto

```
flask run
ou
python app.py
```

# Testando a API

Importe a coleção de testes (Postman ou Bruno) localizada em:

`docs/api_collections/nasa_api_collection.json`
