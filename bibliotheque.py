from exception import LivreDejaPresent, LivreIntrouvable

class Bibliotheque:
    def __init__(self, stockage):
        self.stockage = stockage
        self._livres = stockage.charger()
        
    def ajouter(self, livre):
        if livre in self._livres:
            raise LivreDejaPresent(livre.titre)
        self._livres.append(livre)
        self.stockage.sauvegarder(self._livres)
        
    def trouver(self, titre):
        for l in self._livres:
            if titre == l.titre:
                return l
        raise LivreIntrouvable(titre)
    
    def supprimer(self, titre):
        livre = self.trouver(titre)
        self._livres.remove(livre)
        self.stockage.sauvegarder(self._livres)
        
    def lister(self):
        return sorted(self._livres, reverse=True)
    
    def __len__(self):
        return len(self._livres)