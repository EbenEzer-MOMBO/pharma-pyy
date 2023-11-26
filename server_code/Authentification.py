import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import datetime
import random
import string


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

def generate_unique_id(length=3):
    characters = string.ascii_letters + string.digits  # Chars possibles pour l'ID
    unique_id = ''.join(random.choice(characters) for _ in range(length))
    return unique_id

#Produit==========================

@anvil.server.callable
def ListeProduits():
  return app_tables.produit.search()

@anvil.server.callable
def RechercherProduit(produit):
    # Rechercher les clients dont le nom commence par le texte entré
    results = [row for row in app_tables.produit.search() if row['libelle'].lower().startswith(produit.lower())]
    return results

@anvil.server.callable
def ModifierProduit(produit, libelle, qte, prix):
  produit.update(libelle=libelle, qte=qte, prix=prix, date_ajout=datetime.date.today())

@anvil.server.callable
def AjouterProduit(libelle, qte, prix):
    new_id = generate_unique_id(length=3)

    # Obtenir la date actuelle
    date_ajout = datetime.date.today()

    # Ajouter une nouvelle ligne avec le nouvel identifiant et la date actuelle
    app_tables.produit.add_row(id=new_id, libelle=libelle, qte=qte, prix=prix, date_ajout=date_ajout)

@anvil.server.callable
def SupprimerProduit(produit):
  produit.delete()

  
#Vente==========================

@anvil.server.callable
def ListeProduitsDropdown():
    produits = app_tables.produit.search()
    return [(produit['libelle'], produit['prix']) for produit in produits if produit['prix'] is not None and produit['prix'] > 0]

@anvil.server.callable
def ArchiverVente(vente):
  vente.delete()

@anvil.server.callable
def ListeVentes():
  return app_tables.vente.search()

@anvil.server.callable
def AjouterVente(nom, produit, prix, qte):
    id = generate_unique_id()
    delivre_le = datetime.date.today()
    prix_numerique = float(prix) if isinstance(prix, str) else prix
    total = prix_numerique * qte

    # Récupérer le produit de la table produit
    produit_row = app_tables.produit.get(libelle=produit)

    if produit_row is not None:
        # Vérifier si la quantité en stock est suffisante pour la vente
        if produit_row['qte'] >= qte:
            # Déduire la quantité vendue du stock
            nouvelle_qte = produit_row['qte'] - qte
            produit_row.update(qte=nouvelle_qte)  # Mettre à jour la quantité dans la table produit

            # Ajouter une nouvelle ligne dans la table vente
            app_tables.vente.add_row(id=id, nom_complet=nom, produit=produit, qte=qte, delivre_le=delivre_le, total=total)
            return True  # Indiquer que la vente a été effectuée avec succès
        else:
            return False  # Indiquer que la quantité en stock est insuffisante
    else:
        # Le produit n'existe pas dans la table produit
        print("Le produit n'existe pas dans la table produit.")
        return None  # Indiquer qu'il y a eu un problème lors de la recherche du produit



#Commande==========================

@anvil.server.callable
def ListeCommandesAttente():
  return app_tables.commande_attente.search()

@anvil.server.callable
def ListeCommandesRecues():
  return app_tables.commande_recues.search()

@anvil.server.callable
def AjouterCommande(produit, qte):
  id = generate_unique_id()
  ajoute_le = datetime.date.today()
  app_tables.commande_attente.add_row(id=id, produit=produit, qte=qte, modifie_le=ajoute_le)

@anvil.server.callable
def ConfirmerCommande(commande):
    id = generate_unique_id()
    recu_le = datetime.date.today()

    libelle_commande = commande['produit'].lower()

    produit = next((prod for prod in app_tables.produit.search() if prod['libelle'].lower() == libelle_commande), None)

    if produit is not None:
        nouvelle_qte = produit['qte'] + commande['qte']
        produit.update(qte=nouvelle_qte)

        app_tables.commande_attente.get(id=commande['id']).delete()

        app_tables.commande_recues.add_row(produit=commande['produit'], qte=commande['qte'], id=id, recu_le=recu_le)
    else:
        new_id = generate_unique_id()
        # Ajouter une nouvelle entrée dans la table produit avec un nouvel ID et la date d'ajout
        app_tables.produit.add_row(libelle=commande['produit'], qte=commande['qte'], id=new_id, date_ajout=recu_le, prix=0)
        app_tables.commande_attente.get(id=commande['id']).delete()
        # Ajouter une nouvelle ligne à la table de destination (commande_recues)
        app_tables.commande_recues.add_row(produit=commande['produit'], qte=commande['qte'], id=id, recu_le=recu_le)


@anvil.server.callable
def AnnulerCommande(commande):
  commande.delete()


#Client==========================

@anvil.server.callable
def ListeClients():
  return app_tables.client.search()

@anvil.server.callable
def RechercherClient(client):
    # Rechercher les clients dont le nom commence par le texte entré
    results = [row for row in app_tables.client.search() if row['nom_complet'].lower().startswith(client.lower())]
    return results

@anvil.server.callable
def AjoutClient(nom, adresse):
    new_id = generate_unique_id(length=3)
    
    app_tables.client.add_row(id=new_id, nom_complet=nom, adresse=adresse)

@anvil.server.callable
def ModifierClient(client, nom_complet, adresse):
  client.update(nom_complet=nom_complet, adresse=adresse)

@anvil.server.callable
def SupprimerClient(client):
  client.delete()