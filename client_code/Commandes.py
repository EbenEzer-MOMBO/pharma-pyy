from ._anvil_designer import CommandesTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import random
import string
from .State import clients

class Commandes(CommandesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.liste_attente.items = anvil.server.call('ListeCommandesAttente')
    self.liste_recu.items = anvil.server.call('ListeCommandesRecues')

  

  

  def primary_color_1_click(self, **event_args):
    open_form('Stock')

  def primary_color_1_copy_1_copy_2_click(self, **event_args):
    open_form('Ventes')

  def primary_color_1_copy_1_click(self, **event_args):
    open_form('Clients')

  def button_1_click(self, **event_args):
    produit = self.text_box_1.text
    qte = self.text_box_2.text
    if produit!='' and qte!='':
      anvil.server.call('AjouterCommande', produit, qte)
      self.liste_attente.items = anvil.server.call('ListeCommandesAttente')
      self.text_box_1.text = ''
      self.text_box_2.text = ''