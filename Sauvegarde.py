from abc import ABC, abstractmethod
from Livres import Livre, livre_depuis_dict
from dataclasses import asdict
import json

class Stockage(ABC):
    @abstractmethod
    def charger(self):
        ...
        
    @abstractmethod
    def sauvegarder(self, liste):
        ...
        
class StockageJSON(Stockage):
    def __init__(self, chemin):
        self.chemin = chemin
        
    def charger(self):
        try:
            with open(self.chemin, "r", encoding="utf-8") as f:
                return [livre_depuis_dict(l) for l in json.load(f)]
        except:
            return []
        
    def sauvegarder(self, liste):
        with open (self.chemin, "w", encoding="utf-8") as f:
            for l in liste:
                json.dump(asdict(l), f, indent=2)