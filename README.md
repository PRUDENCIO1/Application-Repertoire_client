# shell
pip install Flask Flask-SQLAlchemy# shell
pip install Flask Flask-SQLAlchemy# shell
python # Répertoire Client

Application web simple en Flask pour gérer un répertoire de clients (CRUD).

## Description
Petite application demonstrative utilisant Flask et SQLite. Permet d'ajouter, modifier, supprimer et lister des clients via des templates Jinja2.

## Fonctionnalités
- Lister tous les clients
- Ajouter un client
- Modifier un client
- Supprimer un client

## Prérequis
- Node/NPM non requis
- Python 3.8+
- pip

## Installation (local)
1. Créer et activer un environnement virtuel :
```bash
# shell
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
.venv\Scripts\activate     # Windows (PowerShell)

2. Installer les dépendances :
Initialiser la base (création automatique à la première exécution) et lancer l'application :
L'application sera disponible par défaut sur http://127.0.0.1:5000

Structure du projet
repertoire_client/app.py — point d'entrée Flask, routes principales (voir index, add_client, edit_client, delete_client)
repertoire_client/models.py — définition du modèle Client et initialisation de db
repertoire_client/templates/ — templates Jinja2 utilisés par l'app :
base.html
index.html
add_client.html
edit_client.html
Utilisation
Ouvrir la page d'accueil pour voir la liste des clients.
Cliquer sur "Ajouter" pour créer un nouveau client.
Cliquer sur "Modifier" à côté d'un client pour éditer ses informations.
Cliquer sur "Supprimer" pour retirer un client (confirmation simple côté navigateur).
Développement
Modifier les templates dans repertoire_client/templates/.
Le modèle principal est dans Client.
Pour tests manuels, lancer python repertoire_client/app.py et utiliser le navigateur.
Déploiement
Pour un déploiement basique : utiliser un serveur WSGI (gunicorn/uWSGI) et configurer une base SQLite ou remplacer par une base plus adaptée (Postgres/MySQL).
Améliorations possibles
Validation des formulaires côté serveur et client
Pagination et recherche
Authentification (Flask-Login)
Migration de la base (Flask-Migrate)
Tests unitaires / intégration
Licence
MIT — adapter selon besoins.

Contact
Projet local — voir les fichiers sources pour plus de détails.
Email: prudencioalcarino@gmail.com
