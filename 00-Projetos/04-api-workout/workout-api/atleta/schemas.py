from typing import Annotated
from pydantic import  Field, PositiveFloat
from contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta',max_length=50)] #como seria usar o parametro 'examples' aqui?
    cpf: Annotated[str, Field(description='CPF do atleta', max_length=11)] #aqui pode ter um validator 
    idade: Annotated[int, Field(description='Idade do atleta', max_length=2)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta')]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta')]
    sexo: Annotated[str, Field(description='Sexo do atleta', examples=['M', 'F'], max_length=1)]
