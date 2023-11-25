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
    self.drop_client.items = clients
    produits = anvil.server.call('ListeProduitsDropdown')
    self.drop_prod.items = [libelle for libelle, prix in produits]
    self.text_prix.text = [prix for prix, prix in produits]

  def drop_prod_change(self, **event_args):
    produits = anvil.server.call('ListeProduitsDropdown')
    selected_libelle = self.drop_prod.selected_value  # Récupère le libellé sélectionné
    # Recherche le prix correspondant au libellé sélectionné dans 'produits'
    selected_prix = next((prix for libelle, prix in produits if libelle == selected_libelle), None)
    if selected_prix is not None:
      self.text_prix.text = str(selected_prix)  # Assigner le prix au champ de texte
    else:
      self.text_prix.text = ""  # Effacer le champ si aucun prix correspondant n'est trouvé

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def button_1_click(self, **event_args):
    nom_complet = self.drop_client.selected_value
    produit = self.drop_prod.selected_value
    prix = self.text_prix.text
    qte = self.text_qte.text
    if nom_complet!='' and produit!='' and prix!='' and qte!='':
      anvil.server.call('AjouterVente', nom_complet, produit, prix, qte)
      #rafraichir
      self.repeating_panel_1.items = anvil.server.call('ListeVentes')
      #effacer les champs
      self.drop_client.text = ''
      self.drop_prod.text = ''
      self.text_prix.text = ''
      self.text_qte.text = ''
    else:
      alert('Veuillez remplir tous les champs !')

  def primary_color_1_click(self, **event_args):
    open_form('Stock')

  def primary_color_1_copy_1_copy_1_click(self, **event_args):
    open_form('Commandes')

  def primary_color_1_copy_1_copy_2_click(self, **event_args):
    open_form('Ventes')
