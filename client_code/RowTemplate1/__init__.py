from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def text_box_2_pressed_enter(self, **event_args):
    self.ModifierClient()

  def text_box_1_pressed_enter(self, **event_args):
    self.ModifierClient()
    
  def ModifierClient(self):
    if self.text_box_1.text!="" and self.text_box_2.text!="":
      modifierClient = anvil.server.call(
        'ModifierClient',
        self.item,
        nom_complet=self.text_box_1.text,
        adresse=self.text_box_2.text,
      )
      alert('Modifié avec succès !')
    else:
      alert('Veuillez remplir tous les champs !')

  def button_1_click(self, **event_args):
    confirmer = confirm('Supprimer le client ?')
    if confirmer:
      anvil.server.call('SupprimerClient', self.item)
      open_form('Clients')
