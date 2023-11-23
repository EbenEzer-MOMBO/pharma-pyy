import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import datetime
import random
import string

@anvil.server.callable
def ListeProduits():
  return app_tables.produit.search()

@anvil.server.callable
def ModifierProduit(produit, libelle, qte, prix):
  produit.update(libelle=libelle, qte=qte, prix=prix, date_ajout=datetime.date.today())

def generate_unique_id(length=3):
    characters = string.ascii_letters + string.digits  # Chars possibles pour l'ID
    unique_id = ''.join(random.choice(characters) for _ in range(length))
    return unique_id

@anvil.server.callable
def AjouterProduit(libelle, qte, prix):
    new_id = generate_unique_id(length=3)

    # Obtenir la date actuelle
    date_ajout = datetime.date.today()

    # Ajouter une nouvelle ligne avec le nouvel identifiant et la date actuelle
    app_tables.produit.add_row(id=new_id, libelle=libelle, qte=qte, prix=prix, date_ajout=date_ajout)

@anvil.server.callable
def SupprimerProduit(produit):
  produit.delete()