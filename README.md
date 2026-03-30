# 💣 Mines Weeper

Un jeu de démineur développé en Python avec l'interface Tkinter.

Projet réalisé par **Angelo**, **Alya** et **Childebert**.

---

## 🎮 Fonctionnalités

- Interface graphique moderne avec Tkinter
- Animation parachute au clic (soldat qui tombe)
- Placement intelligent des mines (premier clic toujours sûr)
- Système de flood fill (révélation en cascade)
- Gestion des drapeaux et points d'interrogation
- Différents niveaux de difficulté (redimensionnable)
- Compteur de mines restantes
- Détection de victoire et défaite

## 🛠 Technologies utilisées

- **Python 3**
- **Tkinter** (interface graphique)
- Architecture Backend / Frontend séparée

## 📁 Structure du projet
MinesWeeper/
├── main.py                 # Point d'entrée du jeu
├── frontend.py             # Interface graphique (Tkinter)
├── backend/
│   ├── init.py
│   ├── board.py            # Logique du plateau
│   ├── cell.py             # Classe Cellule
│   └── game.py             # Gestion du jeu (optionnel)
├── README.md
└── .gitignore
text## 🚀 Comment lancer le jeu

1. Clone le repository ou ouvre le dossier du projet
2. Assure-toi d'avoir Python 3 installé
3. Exécute la commande suivante :

```bash
python main.py
🎯 Commandes du jeu

Clic gauche : Révéler une case (avec animation parachute)
Clic droit : Poser / enlever un drapeau ou point d'interrogation
Boutons du haut : Changer la difficulté, Rejouer, Son

👥 Contributeurs

Angelo
Alya
Childebert