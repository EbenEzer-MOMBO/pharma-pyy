from ._anvil_designer import ClientsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Clients(ClientsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = anvil.server.call('ListeClients')
    # Any code you write here will run when the form opens.

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    pass
