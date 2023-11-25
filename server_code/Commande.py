import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import datetime
import random
import string

def generate_unique_id(length=4):
    characters = string.ascii_letters + string.digits  # Chars possibles pour l'ID
    unique_id = ''.join(random.choice(characters) for _ in range(length))
    return unique_id

@anvil.server.callable
def ListeCommandesAttente():
  return app_tables.commande_attente.search()

@anvil.server.callable
def ListeCommandesRecues():
  return app_tables.commande_recues.search()

@anvil.server.callable
def AjouterCommande(produit, qte):
  id = generate_unique_id()
  ajoute_le = datetime.date.today()
  app_tables.commande_attente.add_row(id=id, produit=produit, qte=qte, modifie_le=ajoute_le)

@anvil.server.callable
def ConfirmerCommande(commande):
  id = generate_unique_id()
  recu_le = datetime.date.today()
  app_tables.commande_recues.add_row(produit=commande['produit'], qte=commande['qte'], id=id, recu_le=recu_le)

@anvil.server.callable
def AnnulerCommande(commande):
  commande.delete()