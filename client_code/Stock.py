from ._anvil_designer import StockTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Stock(StockTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = anvil.server.call('ListeProduits')
    # Any code you write here will run when the form opens.

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def button_1_click(self, **event_args):
    libelle = self.libelle.text
    qte = self.qte.text
    prix = self.prix.text
    if libelle!='' and qte!='' and prix!='':
      anvil.server.call('AjouterProduit', libelle, qte, prix)
      #rafraichir
      self.repeating_panel_1.items = anvil.server.call('ListeProduits')
      #effacer les champs
      self.libelle.text = ''
      self.qte.text = ''
      self.prix.text = ''
    else:
      alert('Veuillez remplir tous les champs !')

  def primary_color_1_copy_1_click(self, **event_args):
    open_form('Clients')
