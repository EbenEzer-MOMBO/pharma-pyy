from ._anvil_designer import ClientsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import random
import string

class Clients(ClientsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = anvil.server.call('ListeClients')
    # Any code you write here will run when the form opens.

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def button_1_click(self, **event_args):
    nom_complet = self.nom_complet.text
    adresse = self.adresse.text
    if nom_complet!='' and adresse!='':
      anvil.server.call('AjoutClient', nom_complet, adresse)
      #rafraichir
      self.repeating_panel_1.items = anvil.server.call('ListeClients')
      #effacer les champs
      self.nom_complet.text = ''
      self.adresse.text = ''
    else:
      alert('Veuillez remplir tous les champs !')

  def primary_color_1_click(self, **event_args):
    open_form('Stock')

  def primary_color_1_copy_1_copy_1_click(self, **event_args):
    open_form('Commandes')

  def primary_color_1_copy_1_copy_2_click(self, **event_args):
    open_form('Ventes')

  def text_box_1_change(self, **event_args):
    nom = self.text_box_1.text.lower()  # Convertir en minuscules
    if nom == '':
      self.repeating_panel_1.items = anvil.server.call('ListeClients')
    results = anvil.server.call('RechercherClient', nom)
    self.repeating_panel_1.items = results

    
