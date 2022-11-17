"""Module Quoridor

Functions:
    * analyser_commande - Génère un interpréteur de commande.
    * formater_légende - Formater la représentation graphique du damier.
    * formater_damier - Formater la représentation graphique de la légende.
    * formater_jeu - Formater la représentation graphique d'un jeu.
    * formater_les_parties - Formater la liste des dernières parties.
    * récupérer_le_coup - Demander le prochain coup à jouer au joueur.
"""
import argparse


def analyser_commande():
    """Génère un interpréteur de commande.

    Returns:
        Namespace: Un objet Namespace tel que retourné par parser.parse_args().
                   Cette objet aura l'attribut «idul» représentant l'idul du joueur
                   et l'attribut «parties» qui est un booléen True/False.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('idul', type=str, default=None, help='IDUL du joueur')
    # Complétez le code ici
    args = parser.parse_args()
    # vous pourriez aussi avoir à ajouter des arguments dans ArgumentParser(...)

    return parser.parse_args()


def formater_légende(joueurs):
    """Formater la représentation graphique de la légende.

    Args:
        joueurs (list): Liste de dictionnaires représentant les joueurs.

    Returns:
        str: Chaîne de caractères représentant la légende.
    """
    
    x = joueurs
    nb_murs_joueur1 = x[0]['murs']
    nb_murs_automate = x[0]['murs']
    nom_IDUL = x[0]['nom']
    nom_automate = x[1]['nom']
    murs_IDUL = nb_murs_joueur1*'|'
    murs_automate = nb_murs_automate*'|'
    Légende = ("Légende:\n"   f"   1={nom_IDUL},  murs={murs_IDUL}\n"   f"   2={nom_automate}, murs={murs_automate}\n")
    return Légende


def formater_damier(joueurs, murs):
    """Formater la représentation graphique du damier.

    Args:
        joueurs (list): Liste de dictionnaires représentant les joueurs.
        murs (dict): Dictionnaire représentant l'emplacement des murs.

    Returns:
        str: Chaîne de caractères représentant le damier.
    """
    
    damier_vide = (
        "   -----------------------------------\n"
        "9 | .   .   .   .   2   .   .   .   . |\n"
        "  |                                   |\n"
        "8 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "7 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "6 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "5 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "4 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "3 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "2 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "1 | .   .   .   .   1   .   .   .   . |\n"
        "--|-----------------------------------\n"
        "  | 1   2   3   4   5   6   7   8   9\n"
    )
    return damier_vide
           


def formater_jeu(état):
    """Formater la représentation graphique d'un jeu.

    Doit faire usage des fonctions formater_légende et formater_damier.

    Args:
        état (dict): Dictionnaire représentant l'état du jeu.

    Returns:
        str: Chaîne de caractères représentant le jeu.
    """
    from quoridor import formater_légende 
    from quoridor import formater_damier
    return formater_légende(état['joueurs']) + formater_damier(état['joueurs'], état['murs'])


def formater_les_parties(parties):
    """Formater une liste de parties
    L'ordre rester exactement la même que ce qui est passé en paramètre.

    Args:
        parties (list): Liste des parties

    Returns:
        str: Représentation des parties
    """
    pass


def récupérer_le_coup():
    """Récupérer le coup

    Returns:
        tuple: Un tuple composé d'un type de coup et de la position.
               Le type de coup est une chaîne de caractères.
               La position est une liste de 2 entier [x, y].
    Examples:
        Quel type de coup voulez-vous jouer? ('D', 'MH', 'MV'):
        Donnez la position où appliquer ce coup (x,y): 2,6
    """
    pass
