# 📚 Formation Python-Django - 0 (OOB)

## 🚀 Résumé

Bienvenue dans la première journée du projet **Python-Django - OOB** (Object-Oriented Basics) !
Aujourd’hui, vous partez à la conquête de la Silicon Valley, fort·e de vos nouvelles compétences en programmation orientée objet (POO) avec Python. Ce projet vous fait découvrir les fondements de la POO, la manipulation de fichiers, la création de classes, l'héritage, et la modélisation de structures HTML.

---

## 📺 Table des matières

* [Préambule](#préambule)
* [Règles communes](#règles-communes)
* [Règles spécifiques](#règles-spécifiques)
* [Liste des exercices](#exercices)
---

## 💙 Préambule

*"Join us now and share the software; you’ll be free, hackers, you’ll be free."*
Un hommage à la **Free Software Song** pour démarrer cette aventure dans l’esprit du logiciel libre.

---

## ⚙️ Règles communes

* Travail à réaliser **dans une machine virtuelle** avec tous les outils nécessaires.
* Respect de la **structure de fichiers et dossiers** demandée.
* Aucune **erreur critique** ne doit apparaître (segfault, double free, etc.).
* Tout le code doit être **testable** et **testé**.
* Le dépôt Git est la **source unique de vérité** pour l’évaluation.

---

## 📌 Règles spécifiques

* Aucun code dans le scope global.
* Les fichiers `.py` doivent se terminer par :

  ```python
  if __name__ == '__main__':
      # Tests ici
  ```
* **Aucune exception non catchée**.
* **Imports strictement limités** selon les consignes des exercices.
* Utilisation exclusive de **Python 3**.

---

## 🧩 Exercices

### 📜 Ex00 - À la conquête de la Silicon Valley

Développez un moteur de template HTML à partir d’un fichier `.template` et d’un fichier `settings.py`.

### ☕ Ex01 - Intern et café pas terrible

Création de la classe `Intern` et d’un système simple de gestion de tâches avec exceptions.

### 🍵 Ex02 - 5 classes 1 cup

Création de classes de boissons chaudes dérivées de `HotBeverage`, chacune avec sa propre personnalité.

### 🛠️ Ex03 - Glorious coffee machine

Implémentation d’une `CoffeeMachine` capable de tomber en panne et de se faire réparer, avec gestion aléatoire du service.

### 🧱 Ex04 - Base class pour HTML

Modélisation d’éléments HTML avec une classe `Elem` et gestion propre des attributs et contenus.

### 🧩 Ex05 - HTML sans effort

Création de classes spécialisées (`html`, `body`, `div`, etc.) héritant de `Elem` pour simplifier la génération HTML.

### 🔍 Ex06 - Validation HTML

Implémentation d’une classe `Page` capable de **valider structurellement** une page HTML selon un ensemble de règles strictes.


## 🧠 Remarques

Ce projet est une excellente base pour :

* Comprendre les principes de **la POO en Python**
* Modéliser des objets complexes (comme le HTML)
* Gérer des erreurs proprement
* Organiser un projet sur GitHub

Bonne chance, futur·e développeur·se de la Silicon Valley 🌿
