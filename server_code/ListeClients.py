import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import random

@anvil.server.callable
def ListeClients():
  return app_tables.client.search()


@anvil.server.callable
def AjoutClient(nom, adresse):
    # Récupérer toutes les lignes de la table
    rows = app_tables.client.search()

    if rows:
        # Trouver le maximum des ID existants
        max_id = max(row['id'] for row in rows)
        new_id = max_id + 1
    else:
        # Si la table est vide, commencer par 1
        new_id = 1

    # Ajouter une nouvelle ligne avec le nouvel identifiant
    app_tables.client.add_row(id=new_id, nom_complet=nom, adresse=adresse)
