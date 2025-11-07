from datetime import datetime, UTC
from fastapi import FastAPI

app = FastAPI()

@app.get('/posts/{framework}')
def read_posts(framework):
    return {'posts': [{'title': f'criando uma aplicacao com {framework}', 'date': datetime.now(UTC)},
                      {'title': f'Testando a nova versão de {framework}', 'date': datetime.now(UTC)}
                      ]
            }

@app.get('/posts/type/{framework}') #-> com tipagem nos parametros:
def read_posts2(framework: int):
    return {'posts': [{'title': f'testando {framework} como tipo', 'date': datetime.now(UTC)},
                      {'title': f'tentando {framework}', 'date': datetime.now(UTC)}
                      ]
            }
# ROTAS E ENDPOINTS: QUERY PARAMETERS

fake_db = [
    {'title': "Criando uma aplicacao com Django", 'date': datetime.now(UTC)},
    {'title': "Criando uma aplicacao com Django", 'date': datetime.now(UTC)}
]

@app.get("/posts/fakedb")
def read_posts3():
    return fake_db

