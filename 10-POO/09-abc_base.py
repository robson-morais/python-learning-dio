from abc import ABC, abstractmethod

class Pessoa(ABC):

    @abstractmethod
    def falar(self):
        pass
    
    @abstractmethod
    def andar(self):
        pass

    @property
    @abstractmethod
    def sexo(self):
        pass

class Crianca(Pessoa):

    def falar(self):
        print("Falando...")    

    def andar(self):
        print("Andando...")
    
c = Crianca()
c.falar()
c.andar()