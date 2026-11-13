# Bibliothèque

Gestionnaire de livres en Python (programmation orientée objet) :
ajout, recherche, suppression et liste triée par note, avec sauvegarde en JSON.

## Ce que montre ce projet

- Classes et héritage (`Livre`, `LivreNumerique`), dataclasses
- Séparation des rôles : modèle, stockage, gestion
- Classe abstraite `Stockage` et implémentation `StockageJSON`
- Exceptions personnalisées
- Tests automatiques avec pytest

## Installation

    git clone <adresse du dépôt>
    cd <dossier>
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Utilisation

    python main.py

## Structure

- `livres.py` : les classes Livre et LivreNumerique
- `sauvegarde.py` : le stockage JSON
- `bibliotheque.py` : la gestion de la collection
- `exceptions.py` : les erreurs du projet
- `main.py` : exemple d'utilisation
