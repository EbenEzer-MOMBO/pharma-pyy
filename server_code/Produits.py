import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import datetime

@anvil.server.callable
def ListeProduits():
  return app_tables.produit.search()

@anvil.server.callable
def ModifierProduit(produit, libelle, qte, prix):
  produit.update(libelle=libelle, qte=qte, prix=prix, date_ajout=datetime.date.today())

@anvil.server.callable
def AjouterProduit(libelle, qte, prix):
    # Récupérer toutes les lignes de la table
    rows = app_tables.produit.search()

    if rows and any('id' in row for row in rows):  # Vérifier si 'id' existe dans les lignes
        # Trouver le maximum des ID existants
        max_id = max(row['id'] for row in rows)
        new_id = max_id + 1
    else:
        # Si la table est vide ou si la colonne 'id' est absente, commencer par 1
        new_id = 1

    # Obtenir la date actuelle
    date_ajout = datetime.date.today()

    # Ajouter une nouvelle ligne avec le nouvel identifiant et la date actuelle
    app_tables.produit.add_row(id=new_id, libelle=libelle, qte=qte, prix=prix, date_ajout=date_ajout)