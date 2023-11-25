from ._anvil_designer import RowTemplate4Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate4(RowTemplate4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    confirmer = confirm('Annuler la commande ?')
    if confirmer:
      anvil.server.call('AnnulerCommande', self.item)
      open_form('Commandes')

  def button_1_click(self, **event_args):
    confirmer = confirm('La commande a bien été reçue ?')
    if confirmer:
      anvil.server.call('ConfirmerCommande', self.item)
      open_form('Commandes')
