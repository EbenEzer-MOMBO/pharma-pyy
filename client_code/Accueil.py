from ._anvil_designer import AccueilTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Accueil(AccueilTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def primary_color_1_copy_1_click(self, **event_args):
    open_form('Clients')

  def primary_color_1_click(self, **event_args):
    open_form('Stock')

  def primary_color_1_copy_1_copy_2_click(self, **event_args):
    open_form('Ventes')

  def primary_color_1_copy_1_copy_1_click(self, **event_args):
    open_form('Commandes')
