"""Module d'API du jeu Quoridor

Attributes:
    URL (str): Constante représentant le début de l'url du serveur de jeu.

Functions:
    * lister_parties - Récupérer la liste des parties reçus du serveur.
    * débuter_partie - Créer une nouvelle partie et retourne l'état de cette dernière.
    * récupérer_partie - Retrouver l'état d'une partie spécifique.
    * jouer_coup - Exécute un coup et retourne le nouvel état de jeu.
"""

import requests


BASE_URL = "https://pax.ulaval.ca/quoridor/api/v2/"


def lister_parties(idul, SECRET):
    """Lister les parties

    Args:
        idul (str): idul du joueur
        secret (str): secret récupérer depuis le site de PAX

    Raises:
        PermissionError: Erreur levée lorsque le serveur retourne un code 401.
        RuntimeError: Erreur levée lorsque le serveur retourne un code 406.
        ConnectionError: Erreur levée lorsque le serveur retourne un code autre que 200, 401 ou 406

    Returns:
        list: Liste des parties reçues du serveur,
             après avoir décodé le json de sa réponse.
    """
    import requests

    BASE_URL = 'https://pax.ulaval.ca/quoridor/api/v2/'

    rep = requests.get(BASE_URL+'parties', auth=(idul, SECRET))

    if rep.status_code == 200:
        # la requête s'est déroulée normalement;
        # décoder le JSON et afficher la liste de parties
        rep = rep.json()
        return(rep)

    elif rep.status_code == 401:
        # Votre requête est invalide;
        # décoder le JSON et afficher le message d'erreur
        rep = rep.json()
        raise PermissionError (rep[1])

    elif rep.status_code == 406:
        # Votre requête est invalide;
        # décoder le JSON et afficher le message d'erreur
        raise RuntimeError (rep[1])
        raise(rep)
    else:
        # Une erreur inattendue est survenue
        raise ConnectionError


def débuter_partie(idul, SECRET):
    """Débuter une partie

    Args:
        idul (str): idul du joueur
        secret (str): secret récupérer depuis le site de PAX

    Raises:
        PermissionError: Erreur levée lorsque le serveur retourne un code 401.
        RuntimeError: Erreur levée lorsque le serveur retourne un code 406.
        ConnectionError: Erreur levée lorsque le serveur retourne un code autre que 200, 401 ou 406

    Returns:
        tuple: Tuple constitué de l'identifiant de la partie en cours
            et de l'état courant du jeu, après avoir décodé
            le JSON de sa réponse.
    """
    import requests
    
    BASE_URL = 'https://pax.ulaval.ca/quoridor/api/v2/'

    rep = requests.post(BASE_URL+'partie', auth=(idul, SECRET))

    
    if rep.status_code == 200:
        # la requête s'est déroulée normalement;
        # décoder le JSON et afficher la liste de parties
        rep = rep.json()
        return(rep['id'], rep['état'])
    if rep.status_code == 401:
        # Votre requête est invalide;
        # décoder le JSON et afficher le message d'erreur
        rep = rep.json()
        raise PermissionError (rep[1])

    elif rep.status_code == 406:
        # Votre requête est invalide;
        # décoder le JSON et afficher le message d'erreur
        raise RuntimeError (rep[1])
        raise(rep)
    elif rep.status_code != 406 or rep.status_code != 200 or rep.status_code != 401 :
        # Une erreur inattendue est survenue
        raise ConnectionError
    



def récupérer_partie(id_partie, idul, SECRET):
    """Récupérer une partie

    Args:
        id_partie (str): identifiant de la partie à récupérer
        idul (str): idul du joueur
        secret (str): secret récupérer depuis le site de PAX

    Raises:
        PermissionError: Erreur levée lorsque le serveur retourne un code 401.
        RuntimeError: Erreur levée lorsque le serveur retourne un code 406.
        ConnectionError: Erreur levée lorsque le serveur retourne un code autre que 200, 401 ou 406

    Returns:
        tuple: Tuple constitué de l'identifiant de la partie en cours
            et de l'état courant du jeu, après avoir décodé
            le JSON de sa réponse.
    """
    BASE_URL = 'https://pax.ulaval.ca/quoridor/api/v2/'

    rep = requests.get(BASE_URL+'parties/'+f'<{id_partie}>', auth=(idul, SECRET))
    
    if rep.status_code == 401:
        # Votre requête est invalide;
        # décoder le JSON et afficher le message d'erreur
        rep = rep.json()
        raise PermissionError (rep[1])

    elif rep.status_code == 406:
        # Votre requête est invalide;
        # décoder le JSON et afficher le message d'erreur
        raise RuntimeError (rep[1])
        raise(rep)
    
    elif rep.status_code != 406 or rep.status_code != 200 or rep.status_code != 401 :
        # Une erreur inattendue est survenue
        raise ConnectionError

    return(rep['id'], rep['état'], rep['gagnant']) 

def jouer_coup(id_partie, type_coup, position, idul, SECRET):
    """Jouer un coup

    Args:
        id_partie (str): Identifiant de la partie.
        type_coup (str): Type de coup du joueur :
                            'D' pour déplacer le jeton,
                            'MH' pour placer un mur horizontal,
                            'MV' pour placer un mur vertical;
        position (list): La position [x, y] du coup.
        idul (str): idul du joueur
        secret (str): secret récupérer depuis le site de PAX

    Raises:
        StopIteration: Erreur levée lorsqu'il y a un gagnant dans la réponse du serveur.
        PermissionError: Erreur levée lorsque le serveur retourne un code 401.
        RuntimeError: Erreur levée lorsque le serveur retourne un code 406.
        ConnectionError: Erreur levée lorsque le serveur retourne un code autre que 200, 401 ou 406

    Returns:
        tuple: Tuple constitué de l'identifiant de la partie en cours
            et de l'état courant du jeu, après avoir décodé
            le JSON de sa réponse.
    """
    import requests
    
    BASE_URL = 'https://pax.ulaval.ca/quoridor/api/v2/'

    rep = requests.put(BASE_URL+'jouer', auth=(idul, SECRET),json={
        "id": id_partie,
        "type": type_coup,
        "pos": position,
    })

    rep.json()

   
    
    if rep.status_code == 401:
        # Votre requête est invalide;
        # décoder le JSON et afficher le message d'erreur
        rep = rep.json()
        raise PermissionError ('message')

    elif rep.status_code == 406:
        # Votre requête est invalide;
        # décoder le JSON et afficher le message d'erreur
        rep = rep.json()
        raise RuntimeError (rep['message'])
        
    elif rep.status_code != 406 or rep.status_code != 200 or rep.status_code != 401 :
        # Une erreur inattendue est survenue
        raise ConnectionError
    if rep['gagnant'] != None:
        raise StopIteration (rep['gagnant'])
    return((rep['id']), (rep['état']), (rep['gagnant']))