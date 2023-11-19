from ._anvil_designer import ConnexionTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Connexion(ConnexionTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    email = self.email.text
    password = self.passwd.text
    
    # Appel à la fonction de connexion avec les valeurs des champs texte
    result = anvil.server.call('Connexion', email, password)
    
    # Faites quelque chose avec le résultat, comme afficher un message à l'utilisateur
    if result == "Connexion réussie":
        # Connexion réussie
        print("Connexion réussie !")
        open_form('Accueil')
    else:
        # Connexion échouée
        print("Email ou mot de passe incorrect.")
        # Afficher un message à l'utilisateur ou effectuer d'autres actions
