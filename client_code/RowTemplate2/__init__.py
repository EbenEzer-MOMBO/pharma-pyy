from ._anvil_designer import RowTemplate2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate2(RowTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    anvil.server.call('SupprimerProduit', self.item)
    self.parent.raise_event()

  def text_box_1_pressed_enter(self, **event_args):
    self.ModifierProduit()

  def text_box_2_pressed_enter(self, **event_args):
    self.ModifierProduit()

  def text_box_3_pressed_enter(self, **event_args):
    self.ModifierProduit()

  def ModifierProduit(self):
    if self.text_box_1.text!="" and self.text_box_2.text!="" and self.text_box_3.text!="":
      modifierProduit = anvil.server.call(
        'ModifierProduit',
        self.item,
        libelle=self.text_box_1.text,
        qte=self.text_box_2.text,
        prix=self.text_box_3.text,
      )
      alert('Modifié avec succès !')
    else:
      alert('Veuillez remplir tous les champs !')