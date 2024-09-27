
# WebCommenter

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**WebCommenter** est un outil en ligne de commande qui permet d'analyser les commentaires présents dans le code source HTML d'un site web. Il peut extraire, rechercher et afficher les commentaires HTML et leurs contextes associés dans le code source.

## Table des matières

- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
  - [Options](#options)
  - [Exemples d'utilisation](#exemples-dutilisation)
- [Tests](#tests)
- [Contribution](#contribution)
- [Licence](#licence)

---

## Fonctionnalités

- **Extraction du code source** : Afficher le code source complet d'une page web.
- **Extraction des commentaires HTML** : Extraire uniquement les commentaires HTML présents dans une page web.
- **Recherche dans les commentaires** : Rechercher un mot ou une phrase spécifique dans les commentaires et afficher leur contexte dans le code.
- **Enregistrement des résultats** : Enregistrer les résultats dans un fichier texte pour une consultation ultérieure.

## Prérequis

Avant de commencer, assurez-vous que les outils suivants sont installés :

- **Python 3.x** : [Télécharger Python ici](https://www.python.org/downloads/)
- **Connexion Internet** : Le script récupère le code source des pages web en ligne.

## Installation

Clonez ce dépôt GitHub sur votre machine locale et assurez-vous que Python 3.x est installé.

```bash
git clone https://github.com/Mandarun-creator/WebCommenter.git
cd WebCommenter
```

Aucune dépendance externe supplémentaire n'est nécessaire, car nous utilisons seulement des modules Python intégrés.

## Utilisation

Une fois dans le répertoire du projet, vous pouvez exécuter le script `webcommenter.py` avec différentes options en ligne de commande.

### Options

Voici les principales options disponibles pour utiliser **WebCommenter** :

- `-c` ou `--code` : Afficher tout le code source de la page web.
- `-C` ou `--comment` : Afficher uniquement les commentaires HTML de la page.
- `-S TERM` ou `--search TERM` : Rechercher un mot ou une phrase spécifique dans les commentaires HTML et afficher leur contexte dans le code source.
- `-o FILENAME` ou `--output FILENAME` : Enregistrer les résultats dans un fichier texte.
- `--test` : Exécuter les tests unitaires intégrés.

### Exemples d'utilisation

1. **Afficher tout le code source d'une page web** :

   ```bash
   python3 webcommenter.py -c https://example.com
   ```

2. **Afficher uniquement les commentaires HTML d'une page web** :

   ```bash
   python3 webcommenter.py -C https://example.com
   ```

3. **Rechercher le mot "TODO" dans les commentaires et afficher le contexte du code** :

   ```bash
   python3 webcommenter.py -S "TODO" https://example.com
   ```

4. **Enregistrer les résultats des commentaires dans un fichier `resultat.txt`** :

   ```bash
   python3 webcommenter.py -C -o resultat.txt https://example.com
   ```

## Tests

Vous pouvez exécuter les tests unitaires intégrés pour vérifier le bon fonctionnement du script.

```bash
python3 webcommenter.py --test
```

Cela exécutera des tests unitaires qui valideront plusieurs fonctionnalités, comme l'extraction des commentaires et la recherche dans ceux-ci.

## Contribution

Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet ou corriger des bugs, suivez ces étapes :

1. Forker le dépôt.
2. Créer une branche pour vos modifications.
3. Pousser vos modifications dans la branche.
4. Ouvrir une Pull Request.

Assurez-vous d'inclure des tests unitaires pour tout nouveau code ou fonctionnalité.

## Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus d'informations.

