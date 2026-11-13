from Livres import Livre, LivreNumerique
from Sauvegarde import StockageJSON
from bibliotheque import Bibliotheque
from exception import LivreIntrouvable, LivreDejaPresent
 
if __name__ == "__main__":
    bib = Bibliotheque(StockageJSON("livres.json"))
 

    try:
        bib.ajouter(Livre("Dune", "Herbert", note=5))
        bib.ajouter(LivreNumerique("Python", "X", note=4, taille_mo=12))
    except LivreDejaPresent as e:
        print(e)
 
    print("--- Liste ---")
    for livre in bib.lister():
        print(livre)
 
    try:
        bib.trouver("Dune")
    except LivreIntrouvable as e:
        print(e)
 
    print(len(bib), "livre(s) restant(s)")
