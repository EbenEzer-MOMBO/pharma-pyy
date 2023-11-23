import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import datetime
import random
import string

@anvil.server.callable
def ListeProduitsDropdown():
    produits = app_tables.produit.search()
    return [(produit['libelle'], produit['prix']) for produit in produits]

def generate_unique_id(length=4):
    characters = string.ascii_letters + string.digits  # Chars possibles pour l'ID
    unique_id = ''.join(random.choice(characters) for _ in range(length))
    return unique_id

@anvil.server.callable
def ListeVentes():
  return app_tables.vente.search()

@anvil.server.callable
def AjouterVente(nom, produit, prix, qte):
  id = generate_unique_id()
  delivre_le = datetime.date.today()
  prix_numerique = float(prix) if isinstance(prix, str) else prix
  total = prix_numerique * qte
  app_tables.vente.add_row(id=id, nom_complet=nom, produit=produit, qte=qte, delivre_le=delivre_le, total=total)