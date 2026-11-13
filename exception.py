class LivreIntrouvable(Exception):
    def __init__(self, titre):
        super().__init__(f"Livre '{titre}' introuvable")
        self.titre = titre
        
class LivreDejaPresent(Exception):
    def __init__(self, titre):
        message = f"Le livre '{titre}' est déjà dans la bibliothèque"
        super().__init__(message)
        self.titre = titre
