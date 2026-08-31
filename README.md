# RedFlower-s
Projet regroupant RedFlower's Terminal, l'outil de surveillance PHost et Hackrow-Terminal (développé en Python).

# RedFlower's Terminal & Associated Projects

Projet personnel développé par LUUXO.

Fichier de lancement : RedFlowes.py

---

## 1. RedFlower's Terminal
* **Créateur :** LUUXO
* **Période de développement :** Projet commencé entre 16 et 17 ans, terminé le 22/03/2026.
* **Version actuelle :** RedFlower's 2026 (Version expérimentale)
* **Description :** Terminal expérimental orienté cybersécurité développé en Python. Il regroupe plusieurs outils réseau, d'analyse système et d'apprentissage autour de la sécurité informatique, inspiré des terminaux Linux. Il intègre également des modules du projet Hackrow-Terminal.

### Fonctionnalités et structure
* Interface terminal personnalisée (incluant les modules Hackrow)
* Scan réseau (basé sur Nmap) et analyse du trafic (Wireshark)
* Informations système et réseau
* +4518 lignes de code, 29+ fichiers au total.

### Commandes principales
* `Get-Help` : Affiche la liste des commandes disponibles.
* `Clear` : Efface l'écran du terminal.
* `Run-Hackrow.exe` : Lance le terminal Hackrow intégré.
* `Get-ComputerType` : Affiche les informations détaillées de l'ordinateur.
* `Get-NetworkInfo` : Affiche les informations réseau.
* `-Scan` : Lance un scan de ports sur une cible.
* `-Shark` : Lance une capture réseau sur l'interface active.
* `-Tools` : Affiche les outils utilisés.

### Outils et dépendances utilisés
* **Python** (https://www.python.org/)
* **Visual Studio Code** (https://code.visualstudio.com/)
* **Nmap** (https://nmap.org/)
* **Wireshark** (https://www.wireshark.org/)

---

## 2. PHost (Périphérique Host)
* **Description :** Outil développé pour effectuer une surveillance active des périphériques connectés à un système Windows (USB, imprimantes, smartphones, etc.). Il communique directement avec les interfaces système proches du matériel (WMI – Windows Management Instrumentation).
* **Fonctionnalités clés :** 
  * Détection en temps réel (scan toutes les 100 ms).
  * Affichage des données (nom, classe, fabricant, statut, VID, etc.).
  * Journalisation automatique dans `peripheriques_log.txt`.
* **Détails techniques :**
  * Langage : Python 3
  * Module principal : `wmi`
  * Système : Windows uniquement
  * Base VID intégrée : 100+ marques

---

## 3. Hackrow-Terminal (RedFlower's Edition)
* **Créateur :** LUUXO
* **Date de création initiale :** 2022 - 2023 (Âge lors du développement : 14 - 15 ans)
* **Description :** Terminal basé à l'origine sur Windows 10/11, gérant 3 langues (Français, Anglais, Espagnol). Il intègre un environnement Batch (CMD), une prise en charge partielle de Python et PHost. La version *RedFlower's Edition* apporte une amélioration de la colorimétrie, des corrections de bugs et un renforcement de l'aspect Linux (scan réseau/ports).

---

## Avertissement légal et éducatif
Ces outils ont été conçus dans un cadre personnel, éducatif et expérimental d'apprentissage (Python, réseaux, cybersécurité, automatisation). 
L'utilisateur est seul responsable de l'utilisation qu'il fait des codes et des outils présents dans ce dépôt, dans le respect de la législation en vigueur.
