from typing import Annotated

from pydantic import Field
from contrib.schemas import BaseSchema

class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', max_length=20)]
    endereco: Annotated[str, Field(description='Endereco do centro de treinamento', max_length=60)]
    proprietario: Annotated[str, Field(description='Nome do Proprietario do centro de treinamento', max_length=30)]

