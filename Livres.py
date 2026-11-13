from dataclasses import dataclass, field

@dataclass
class Livre:
    titre : str
    auteur : str
    lu : bool = field(default=False, compare=False)
    note : int = field(default=0)
    type : str = "physique"
    
    def __post_init__(self):
        if not self.titre_valide(self.titre):
            raise ValueError("titre invalide")
        if not 0 <= self.note <= 5:
            raise ValueError("la note doit etre comprise entre 0 et 5")
        
    def marquer_lu(self):
        self.lu = True
    
    @staticmethod
    def titre_valide(titre):
        return bool(titre and titre.strip())
    
    def __eq__(self, value):
        if not isinstance(value, Livre):
            return NotImplemented
        return self.titre == value.titre and self.auteur == value.auteur
    
    def __lt__(self, other):
        if not isinstance(other, Livre):
            return NotImplemented
        return self.note < other.note
    

@dataclass (eq=False)
class LivreNumerique(Livre):
    taille_mo : int = field(kw_only=True)
    type : str = "Numerique"
    
    
def livre_depuis_dict(data):
    if data.get("type") == "Numerique":
        return LivreNumerique(**data)
    return Livre(**data)