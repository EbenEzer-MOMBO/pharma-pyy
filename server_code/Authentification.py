import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


@anvil.server.callable
def Connexion (email, passwd):
  # Récupérer la référence de la Data Table utilisateurs
    table_admin = app_tables.admin
    
    # Vérifier si l'utilisateur existe dans la Data Table avec les identifiants fournis
    admin = table_admin.get(email=email)
    
    # Vérifier si l'utilisateur existe et si le mot de passe correspond
    if admin is not None and admin['mot_de_passe'] == passwd:
        return "Connexion réussie"
    else:
        return "Email ou mot de passe incorrect"