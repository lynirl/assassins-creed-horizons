import abc

class AbstractMiniJeu(abc.ABC):
    #Définition des propriété de classe a faire ici
    
    @abc.abstractclassmethod
    def __init__(self):
        pass

    @abc.abstractclassmethod
    def run_miniJeu(self):
        pass