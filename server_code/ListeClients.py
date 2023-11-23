import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import datetime
import random
import string

@anvil.server.callable
def ListeClients():
  return app_tables.client.search()

def generate_unique_id(length=3):
    characters = string.ascii_letters + string.digits  # Chars possibles pour l'ID
    unique_id = ''.join(random.choice(characters) for _ in range(length))
    return unique_id

@anvil.server.callable
def AjoutClient(nom, adresse):
    new_id = generate_unique_id(length=3)
    
    app_tables.client.add_row(id=new_id, nom_complet=nom, adresse=adresse)

@anvil.server.callable
def ModifierClient(client, nom_complet, adresse):
  client.update(nom_complet=nom_complet, adresse=adresse)

@anvil.server.callable
def SupprimerClient(client):
  client.delete()