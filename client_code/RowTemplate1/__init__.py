from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ModalClient import ModalClient

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def text_box_1_focus(self, **event_args):
    """This method is called when the TextBox gets focus"""
    pass

  def button_1_copy_1_click(self, **event_args):
    client_copy = dict(self.item)
    save_btn = alert(
      content=ModalClient(item=client_copy),
      title="Modifier informations du client",
      large=True,
      buttons=[("Enregistrer", True), ("Annuler", False)],
    )
    if save_btn:
      mise_a_jour_reussie = anvil.server.call('ModifierClient', self.item, client_copy)
      if mise_a_jour_reussie:
          print("Mise à jour réussie côté client")
          self.refresh_data_bindings()
      else:
          print("Échec de la mise à jour côté client")
