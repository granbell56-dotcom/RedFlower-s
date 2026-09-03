# RedFlower's

RedFlower's est un projet Python orienté terminal, mêlant un menu interactif, des utilitaires système et des outils de diagnostic réseau. Le projet contient un “HackRow” multilingue, des modules de surveillance système, un mini scanner réseau, une copie de site web, un dashboard Flask et plusieurs scripts de démonstration / pédagogie.

Ce dépôt est surtout un projet personnel et expérimental, assez orienté Windows, avec une interface ASCII colorée et des outils de console.

## Ce que contient le projet

- menu principal en français / anglais / espagnol
- terminal inspiré de HackRow avec commandes personnalisées
- surveillance de l’ordinateur et des ressources système
- débit réseau upload/download en temps réel
- scan de ports avec Nmap ou fallback socket
- banner grabbing
- capture / copie locale d’un site web
- dashboard web local via Flask
- détection de périphériques Windows via WMI
- mini laboratoire d’injection “simulé”

## Stack technique

- Python 3
- colorama
- psutil
- requests
- beautifulsoup4
- flask
- waitress
- python-nmap
- pyshark
- python-whois
- wmi

## Avertissement important

Ce projet est fourni uniquement à des fins éducatives, de test local et de diagnostic autorisé.

L’utilisation de ces outils sur des systèmes, réseaux, serveurs ou sites sans autorisation explicite est interdite. Les fonctionnalités de scan, de détection réseau et d’extraction d’informations peuvent être sensibles et doivent être utilisées uniquement dans un environnement légalement autorisé.

## Installation

1. Vérifier que Python 3 est installé.
2. Ouvrir un terminal dans le dossier du projet.
3. Installer les dépendances :

```bash
pip install -r requirements.txt
```

4. Vérifier que Nmap est installé si tu veux utiliser les fonctions avancées de scan réseau.

## Lancement

Depuis la racine du projet :

```bash
python RedFlowers.py
```

Le programme principal affiche le logo RedFlower’s puis ouvre le menu principal.

## Structure du dépôt

```text
RedFlowers/
├── RedFlowers.py                # point d'entrée principal
├── Menu.py                      # menu principal
├── Menu_FR.py                   # menu français
├── Menu_ESPA.py                 # menu espagnol
├── Menu_ANGL.py                 # menu anglais
├── Hackrow_RedFlowers.py        # terminal HackRow / choix de langue
├── PONT.py                      # pont de redirection entre menus
├── Computer.py                  # infos système / RAM / CPU / disque / réseau
├── Net_Speed.py                 # mesure de débit réseau
├── Banner_Grabbing.py           # scan/banner grabbing
├── mini_nmap.py                 # mini scanner de ports
├── Copy_Site.py                 # copie d'un site web localement
├── Serveur_IP_Flask.py          # dashboard Flask de métriques réseau / système
├── Injection.py                 # mini laboratoire d'injection graphique / simulé
├── Histoire.py                  # historique du projet
├── PHost_FR.py                  # surveillance des périphériques en français
├── PHost_ESPA.py                # surveillance des périphériques en espagnol
├── PHost_ANGL.py                # surveillance des périphériques en anglais
├── Change_Lang_FR_BATCH.py      # batch FR
├── Change_Lang_FR_CROW.py       # mode Crow FR
├── Change_Lang_FR_PYTHON.py     # mode Python FR
├── Change_Lang_FR_PYTHON_BRIDE.py
├── Change_Lang_ESPA_BATCH.py    # batch ESP
├── Change_Lang_ESPA_CROW.py     # mode Crow ESP
├── Change_Lang_ESPA_PYTHON.py   # mode Python ESP
├── Change_Lang_ESPA_PYTHON_BRIDE.py
├── Change_Lang_ANGL_BATCH.py    # batch EN
├── Change_Lang_ANGL_CROW.py     # mode Crow EN
├── Change_Lang_ANGL_PYTHON.py   # mode Python EN
├── Change_Lang_ANGL_PYTHON_BRIDE.py
├── requirements.txt             # dépendances
├── README.md                    # documentation
├── A_VENIR.txt.txt              # fichier de notes / roadmap
└── __pycache__/                 # cache Python
```

## Modules principaux

### 1. Menu principal et HackRow

Les fichiers `Menu.py`, `Menu_FR.py`, `Menu_ESPA.py`, `Menu_ANGL.py` et `Hackrow_RedFlowers.py` créent l’interface principale du projet.

Ils permettent :

- de choisir la langue,
- d’ouvrir un terminal HackRow,
- d’exécuter des commandes système,
- de manipuler le filesystem,
- de lancer des modes Python / batch / Crow,
- de naviguer entre différents modules.

### 2. Système et surveillance

Le fichier `Computer.py` affiche :

- CPU,
- RAM,
- disque,
- octets réseau,
- système d’exploitation,
- informations sur la machine.

`Net_Speed.py` permet une surveillance temps réel du débit réseau en upload/download.

### 3. Réseau / scan / reconnaissance

- `Banner_Grabbing.py` : scan de service / banner grabbing.
- `mini_nmap.py` : mini scanner de ports, fallback socket, log et support de Nmap.
- `Change_Lang_*` : modes de terminal multi-langue / commandes personnalisées.

### 4. Web / dashboard

- `Serveur_IP_Flask.py` : serveur Flask affichant des métriques réseau/système.
- `Copy_Site.py` : copie locale d’un site web via crawling simple.

### 5. Périphériques Windows

Les fichiers `PHost_FR.py`, `PHost_ESPA.py` et `PHost_ANGL.py` utilisent `wmi` pour surveiller les périphériques USB / matériels connectés à la machine Windows.

### 6. Laboratoire simulé

`Injection.py` contient un mini terminal avec logique de profil utilisateur, permission d’accès et simulation de console d’administration. Il ne s’agit pas d’un vrai outil de piratage, mais d’un environnement pédagogique/simulateur.

## Commandes principales du projet

Le menu principal propose des commandes du style :

- `Get-Help`
- `Clear`
- `Get-Log`
- `Get-ComputerInfo`
- `Get-ComputerType`
- `Get-NetworkInfo`
- `Net-Speed`
- `-Scan`
- `-Banner_Grabbing`
- `-Copy_Site`
- `run-dashboard`
- `-Inject`

Dans le terminal HackRow, on trouve aussi des commandes personnalisées comme :

- `//py`
- `//batch`
- `///crow`
- `//nmap`
- `phost`
- `clear`
- `exit`

## Dépendances système externes

Selon les modules utilisés, il peut être nécessaire d’avoir :

- Nmap installé sur le système,
- accès réseau autorisé,
- Wireshark / pyshark si tu utilises certaines fonctions réseau,
- un système Windows pour les fonctions WMI / périphériques.

## Bonnes pratiques

- Ne pas scanner un système sans autorisation.
- Tester uniquement dans un environnement contrôlé.
- Vérifier les permissions avant chaque action réseau.
- Éviter tout usage sur des services tiers sans consentement.

## Auteur

Projet développé par Luuxo.

## Licence

Aucune licence explicite n’est indiquée dans le dépôt pour le moment.

## Conclusion

RedFlower’s est un projet personnel, visuellement orienté terminal, qui mélange :

- sécurité / diagnostic,
- réseaux,
- système,
- menus custom,
- outils de démonstration.

Il peut servir de base pour un outil de console plus avancé, mais il reste avant tout un projet expérimental et pédagogique.
