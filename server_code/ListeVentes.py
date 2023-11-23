import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def ListeProduitsDropdown():
    produits = app_tables.produit.search()
    return [(produit['libelle'], produit['prix']) for produit in produits]